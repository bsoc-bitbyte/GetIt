from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListProductView.as_view()),
    path('<int:pk>/', views.RetrieveProductView.as_view()),
]
