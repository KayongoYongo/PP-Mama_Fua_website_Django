from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.home_page, name='home_page'),
    path('sign-up', views.sign_up, name='sign_up'),
    path('log-in', views.log_in, name='log_in'),
    path('logout', views.logout_page, name='logout_page')
]