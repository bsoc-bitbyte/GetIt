from rest_framework import serializers
from .models import Ticket
from events.serializers import EventSerializer

class TicketSerializer(serializers.ModelSerializer) :
    event = EventSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = [
            'id',
            'event',
            'buyer',
            'response',
            'purchase_date',
            'status',
            'price',
        ]

        extra_kwargs = {
            'status': {'read_only': True},
            }
