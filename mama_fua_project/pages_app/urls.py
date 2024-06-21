from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path("our-location/", views.location_page, name="our_location"),
    path("contact/", views.contact_page, name='contact_page'),
]