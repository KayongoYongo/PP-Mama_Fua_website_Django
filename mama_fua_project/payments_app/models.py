from bookings_app.models import Booking
from django.conf import settings
from django.db import models

# Create your models here.
class Payments(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"Payment {self.id} for Booking {self.booking.id}"