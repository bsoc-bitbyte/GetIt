from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Event
        fields = [
            "id",
            'title',
            'organizer',
            'description',
            'email',
            'phone',
            'date',
            'time',
            'cover_image',
            'event_type',
            'location',
            'ticket_price',
            'created_at',
            'updated_at'
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            }
    
class EventFormSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Event
        fields = [
            'event',
            'form_fields'
        ]
