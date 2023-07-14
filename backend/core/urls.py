from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', include('auth.urls')),
    path('api/accounts/', include('accounts.urls')),
]
