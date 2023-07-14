from django.urls import path
from .views import CreateAccountView, RetrieveUpdateLoggedInAccountView

urlpatterns = [
    path('', CreateAccountView.as_view()),
    path('me/', RetrieveUpdateLoggedInAccountView.as_view()),
]
