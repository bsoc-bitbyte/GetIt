from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Event
        fields = '__all__'
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            }
    
class EventFormSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Event
        fields = '__all__'
