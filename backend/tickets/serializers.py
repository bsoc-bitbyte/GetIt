from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Ticket
        fields = [
            'id',
            'event',
            'buyer',
            'response',
            'purchase_date',
            'status',
        ]
