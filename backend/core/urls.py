from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from .views import stripe_webhook, upi_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('auth.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/events/', include('events.urls')),
    path('api/tickets/', include('tickets.urls')),
    path('api/stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    path('api/upi/webhook/', upi_webhook, name = 'upi-webhook'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
