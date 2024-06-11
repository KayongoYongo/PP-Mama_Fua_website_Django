from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("create-booking/", views.create_booking, name='create_booking'),
]