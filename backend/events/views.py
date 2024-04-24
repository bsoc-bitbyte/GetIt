from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer, EventFormSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.filter(is_visible=True)
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class EventFormViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventFormSerializer
