import logging

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer
from .token import account_activation_token

logger = logging.getLogger(__name__)

from django.core.mail import send_mail


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('activation_mail.html', {
        'user': user.first_name,
        'domain': "localhost:3000" if settings.DEBUG else settings.FRONTEND_URL,
        'uuid': urlsafe_base64_encode(force_bytes(user.email)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = send_mail(mail_subject, message,settings.EMAIL_HOST_USER ,[to_email])
    logger.info(f"Email sent to {to_email} with response {email}")

class CreateAccountView(CreateAPIView):
    """ View to create accounts """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        activateEmail(self.request, instance, instance.email)


class RetrieveUpdateLoggedInAccountView(APIView):
    """ View to retrieve and change logged in account """
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        # let update be partial
        serializer = AccountSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

def get_account(email) :
    return get_object_or_404(Account, email=email)



class ActivateAccountView(APIView):
    def post(self, request, uidb64, token):
        uid = force_str(urlsafe_base64_decode(uidb64))
        account = get_account(uid)
        if account and account_activation_token.check_token(account, token):
            account.is_active = True
            account.save()
            return Response('Account activated successfully',status=200)
        else:
            return Response('Error while activating',status=400)

