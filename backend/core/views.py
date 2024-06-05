from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import stripe
from django.shortcuts import get_object_or_404
from request_logging.decorators import no_logging

from django.conf import settings
from tickets.models import Ticket
from orders.models import Order

@csrf_exempt
@no_logging
def stripe_webhook(request) :
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', None)
    if not sig_header:
        return HttpResponse(status=400)
    event = None

    try :
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return HttpResponse(status=400)
    
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    
    if event['type'] == 'payment_intent.succeeded':
        payment_intent = event['data']['object']
        ticket_id = payment_intent['metadata']['ticket_id']
        try :
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.status = "purchased"
            ticket.save()
        except Exception as e:
            return HttpResponse(status=400)

    return HttpResponse(status=200) 


@csrf_exempt
@require_POST
@no_logging
def upi_webhook(request) :
    data = request.POST

    status = data.get('status')
    order_id = data.get('p_info')

    order = get_object_or_404(Order, id=order_id)

    order.webhook_response = data
    order.transaction_id = data.get('upi_txn_id')
    order.save()

    order_items = order.order_items.all()

    # WARNING: Assuming to be a ticket purchase
    for item in order_items:
        ticket = item.ticket
        assert isinstance(ticket, Ticket)

        if status == 'success':
            ticket.status = 'purchased'
            ticket.save()
        elif status == 'failure' or status == 'close':
            if ticket.status == 'pending':
                ticket.status = 'failed'
                ticket.save()

    if status == 'success':
        order.status = 'COMPLETED'
    elif status == 'failure' or status == 'close':
        order.status = 'CANCELLED'

    order.save()

    return HttpResponse(status=200)
