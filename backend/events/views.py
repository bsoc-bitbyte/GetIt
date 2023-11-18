from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer, EventFormSerializer

# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventFormViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventFormSerializer