from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse
import stripe

from django.conf import settings
from tickets.models import Ticket
from orders.models import Order

import time

TIMEOUT = 60 * 15 # 15 minutes

@csrf_exempt
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
def upi_webhook(request) :
    data = request.POST

    status = data.get('status')
    created_at = data.get('created_at')
    order_id = data.get('order_id')

    try:
        order = Order.objects.get(id=order_id)
    except:
        return HttpResponse(400)

    order_items = order.order_items

    # need to determine txn timeout due to irregularities in UPI service
    txn_timeout = False
    if created_at + TIMEOUT < time.time():
        txn_timeout = True

    # WARNING: Assuming to be a ticket purchase
    for item in order_items:
        ticket = item.ticket
        assert isinstance(ticket, Ticket)

        if status == 'success':
            ticket.status = 'purchased'
            ticket.save()
        elif status == 'failure' or status == 'close' or txn_timeout:
            if ticket.status == 'pending':
                ticket.status = 'failed'
                ticket.save()
