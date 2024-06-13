from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.user_dashboard, name='user_dashboard'),
    path("create-booking/", views.create_booking, name='create_booking'),
    path("edit-booking/", views.edit_booking, name='edit_booking'),
    path("delete-booking/" , views.delete_booking, name='delete_booking'),
    path("view-my-bookings/", views.view_my_booking, name='view_my_booking'),
]