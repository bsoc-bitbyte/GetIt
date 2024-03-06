import os
from django.conf import settings
import requests
from accounts.models import Account
from rest_framework import viewsets 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
import stripe
from .models import Ticket
from .serializers import TicketSerializer
from rest_framework import status
import uuid

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

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
    
        def post(self, request, *args, **kwargs):

            UPI_API_KEY = os.environ.get('UPI_API_KEY')
            txn_id = generate_txn_id()
            amount = request.data.get('price')
            prod_name = request.data.get('prod_name')

            ## get all account objects
            accounts = Account.objects.all()
            print(accounts)
            account = None
            

            # get account model from email id
            if Account.objects.filter(email=request.data.get('email')).exists():
                account = Account.objects.get(email=request.data.get('email'))
            else:
                return Response({"error": "Account with the given email does not exist."}, status=status.HTTP_404_NOT_FOUND)


            data = {
                "key": UPI_API_KEY,  # Your API Key
                "client_txn_id": txn_id,  # Unique transaction ID
                "amount": amount,  # Amount
                "p_info": prod_name,  # Product Information
                "customer_name": account.first_name + " " + account.last_name,  # Customer Name
                "customer_email": account.email ,
                "customer_mobile": account.phone_number,
                "redirect_url": "http://google.com/",  # Your redirect URL after payment
            }

            responsoe_data = create_upi_gateway(data)

            if responsoe_data.get("status") == True:
                return Response(responsoe_data, status=status.HTTP_200_OK)
            else:
                return Response({
                    "error": "Failed to create UPI gateway",
                    "data": responsoe_data
                }, status=status.HTTP_400_BAD_REQUEST)
                



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
    ## generate a random txn id
    return str(uuid.uuid4())
