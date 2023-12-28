from django.conf import settings
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import status

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class CreatePaymentIntent(APIView):

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        print(request.data)

        try :
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='inr',
                payment_method_types=['card','upi'],
                metadata={
                    'ticket_id': request.data.get('ticket_id')
                }
            )
            return Response({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return Response({
                'error': str(e)
            }, status = status.HTTP_400_BAD_REQUEST)
