from django.conf import settings
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTicketOwner

stripe.api_key = settings.STRIPE_SECRET_KEY


class TicketCreateListRetrieveViewSet(mixins.CreateModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin,
                                      viewsets.GenericViewSet):

    def get_queryset(self):
        # Allows to view only user's tickets when listing
        if self.action == 'list':
            return Ticket.objects.filter(buyer=self.request.user)
        else:
            return Ticket.objects.all()

    serializer_class = TicketSerializer
    permission_classes = (IsAuthenticated, IsTicketOwner)

class CreatePaymentIntent(APIView):

    def post(self, request, *args, **kwargs):
        amount = request.data.get('amount')
        try :
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='inr',
                payment_method_types=['card'],
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
