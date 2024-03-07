import os
from django.conf import settings
import requests
from accounts.models import Account
from accounts.views import get_account
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
import stripe
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsTicketOwner
import uuid
from django.db import transaction
import logging

logger = logging.getLogger(__name__)



stripe.api_key = settings.STRIPE_SECRET_KEY
UPI_API_KEY = os.environ.get('UPI_API_KEY')


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
        
class CreateUPIGateway(APIView):

        @transaction.atomic
        def post(self, request, *args, **kwargs):

            txn_id = generate_txn_id()
            amount = request.data.get('price')
            prod_name = request.data.get('prod_name')
            prod_type = request.data.get('prod_type')
            prod_id = request.data.get("prod_id")
            email = request.data.get('email')

            if not all([txn_id, amount, prod_name, prod_type, prod_id, email]):
                return Response({"error": "Missing required data."}, status=status.HTTP_400_BAD_REQUEST)

            account = get_account(email)
            ticket = create_ticket(prod_id, account.id ,response = {}, status = "pending")
            data = create_upi_data(account, txn_id, amount, prod_name, prod_type, ticket.id)

            

            response_data = create_upi_gateway(data)

            if response_data.get("status") == True:
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to create UPI gateway", "data": response_data}, status=status.HTTP_400_BAD_REQUEST)
                
def create_upi_data(account, txn_id, amount, prod_name, prod_type, ticket_id):
    return {
        "key": UPI_API_KEY,  # Your API Key
        "client_txn_id": txn_id,  # Unique transaction ID
        "amount": amount,  # Amount
        "p_info": prod_name,  # Product Information
        "customer_name": f"{account.first_name} {account.last_name}",  # Customer Name
        "customer_email": account.email,
        "customer_mobile": account.phone_number,
        "redirect_url": "http://google.com/",  # Your redirect URL after payment
        "prod_type": prod_type,
        "ticket_id" : ticket_id # ticket id
    }


def create_upi_gateway(data):
    ## get url from the env
    url = os.environ.get('UPIServer')
    url = url + 'create_order/'

    try :
        response = requests.post(url, data)
        return response.json()

    except Exception as e:
        return {
            "error": str(e)
        }
    
def generate_txn_id():
    """
    Generate a random transaction ID.
    
    Returns:
        str: A UUID4 string.
    """
    return str(uuid.uuid4())

def create_ticket(event_id, buyer_id, response, status):
    """
    Create a new ticket.

    Args:
        event_id (int): The ID of the event.
        buyer_id (int): The ID of the buyer.
        response (dict): The response data.
        status (str): The status of the ticket.

    Returns:
        Ticket: The created ticket object, or None if creation failed.
    """
    try:
        return Ticket.objects.create(
            event_id=event_id,
            buyer_id=buyer_id,
            response=response,
            status=status
        )
    except (TypeError, ValueError) as e:  
        logger.error(f"Failed to create ticket: {e}")
        return None
