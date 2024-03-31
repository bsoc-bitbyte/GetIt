from rest_framework import serializers
from .models import Ticket
from events.serializers import EventSerializer
from events.models import Event

class TicketSerializer(serializers.ModelSerializer) :
    event = EventSerializer(read_only=True)
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Event.objects.all(), source='event', write_only=True)
    class Meta:
        model = Ticket
        fields = [
            'id',
            'event',
            'event_id',
            'buyer',
            'response',
            'purchase_date',
            'status',
            'price',
        ]

        extra_kwargs = {
            'status': {'read_only': True},
            }
