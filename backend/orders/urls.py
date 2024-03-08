from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListCreateOrderView.as_view()),
    path('<int:pk>/', views.RetrieveUpdateDestroyOrderView.as_view()),
]
