from django.urls import path

from merchant import views

urlpatterns = [
    path('', views.merchant_creation)
]