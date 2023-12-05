from django.urls import path, include
from .views import EventViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
]
