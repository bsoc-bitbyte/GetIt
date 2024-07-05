from django.urls import path
from .views import CreateAccountView, RetrieveUpdateLoggedInAccountView, activate

urlpatterns = [
    path('', CreateAccountView.as_view()),
    path('me/', RetrieveUpdateLoggedInAccountView.as_view()),
    path('activate/<uidb64>/<token>', activate, name='activate'),
]
