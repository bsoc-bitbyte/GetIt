import os
from django.conf import settings
import requests
from accounts.views import get_account
from rest_framework import mixins, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe
from .models import Ticket from .serializers import TicketSerializer from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from orders.models import Order, OrderItem
from tickets.models import Ticket
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
            print(request.data)
            request =request.data.get('requestData')
            txn_id = generate_txn_id()
            address = request.get('address')
            email = request.get('email')
            order_items = request.get('order_items')
            phone_number = request.get('phone')

            amount = request.get('price')

            form_response = {
                "txn_id": txn_id,
                "first_name": request.get('first_name'),
                "last_name": request.get('last_name'),
                "email": email,
                "phone_number": phone_number,
                "address": address,
                "roll": request.get('roll'),
                "gender": request.get('gender'),
                "batch" : request.get('batch'),
                "branch": request.get('branch')
            }

            if not all([txn_id, amount, email, phone_number]):
                return Response({"error": "Missing required data."}, status=status.HTTP_400_BAD_REQUEST)

            account = get_account(email)
            order = Order.create_order(account, address)
            add_order_item(order_items, order, account, form_response)
            data = create_upi_data(account, txn_id, amount, phone_number, order.id)

            response_data = create_upi_gateway(data)

            if response_data.get("status") == True:
                order.payment_url = response_data['data']['payment_url']
                order.save()
                return Response(response_data, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Failed to create UPI gateway", "data": response_data}, status=status.HTTP_400_BAD_REQUEST)

def create_upi_data(account, txn_id, amount, phone_number, order_id):
    return {
        "key": os.environ.get('UPI_API_KEY'),
        "client_txn_id": txn_id,  # Unique transaction ID
        "amount": amount,  # Amount
        "p_info": order_id,  # Product Information
        "customer_name": f"{account.first_name} {account.last_name}",  # Customer Name
        "customer_email": account.email,
        "customer_mobile": phone_number if phone_number else account.phone_number,  # Customer Mobile
        "redirect_url": "http://getit.iiitdmj.ac.in/payment/" + str(order_id),  # Your redirect URL after payment
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


def add_order_item(order_items, order, account, response):
    """
    Add a new order item to an order.

    Args:
        order_id (int): The ID of the order.
        ticket_id (int): The ID of the ticket.
        quantity (int): The quantity of the ticket.

    Returns:
        OrderItem: The created order item object, or None if creation failed.
    """
    try:
        for order_item in order_items:
            ticket = Ticket.create_ticket(order_item['id'], account, response)
            order_item = OrderItem.create_order_item(order, ticket, order_item['quantity'])
        
    except (TypeError, ValueError) as e:
        logger.error(f"Failed to create order item: {e}")
        return None
