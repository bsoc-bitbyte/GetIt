from rest_framework import viewsets
from .models import Ticket
from .serializers import TicketSerializer

# Create your views here.

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer