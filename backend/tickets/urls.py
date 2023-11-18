from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import TicketViewSet

router = DefaultRouter()
router.register('', TicketViewSet, basename='ticket')

urlpatterns = [
    path('', include(router.urls)),
]