from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AccountSerializer
from .models import Account
from django.shortcuts import get_object_or_404



class CreateAccountView(CreateAPIView):
    """ View to create accounts """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


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