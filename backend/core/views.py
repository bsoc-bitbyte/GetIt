from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import stripe

from django.conf import settings
from tickets.models import Ticket


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
