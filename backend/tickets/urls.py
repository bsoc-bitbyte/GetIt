from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CreateUPIGateway, TicketCreateListRetrieveViewSet, CreatePaymentIntent

router = DefaultRouter()
router.register('', TicketCreateListRetrieveViewSet, basename='ticket')

urlpatterns = [
    path('create-payment-intent/', CreatePaymentIntent.as_view(), name='create-payment-intent'),
    path('create-upi-gateway/', CreateUPIGateway.as_view(), name='create-upi-gateway'),
    path('', include(router.urls)),
]
