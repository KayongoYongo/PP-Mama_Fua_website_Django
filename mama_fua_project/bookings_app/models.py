from django.conf import settings
from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('ready for pick up', 'Ready for pickup'),
        ('transaction complete', 'Transaction completed')
    ]

    PICKUP_CHOICES = [
        ('8 A.M. to 9 A.M.', '8 A.M. to 9 A.M.'),
        ('9 A.M. to 10 A.M.', '9 A.M. to 10 A.M.'),
        ('10 A.M. to 11 A.M.', '10 A.M. to 11 A.M.'),
        ('11 A.M. to 12 P.M.', '11 A.M. to 12 P.M.'),
        ('12 P.M. to 1 P.M.', '12 P.M. to 1 P.M.'),
        ('2 P.M. to 3 P.M.', '2 P.M. to 3 P.M.'),
        ('3 P.M. to 4 P.M.', '3 P.M. to 4 P.M.')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pickup_date = models.DateField(null=True, blank=True)
    pickup_time = models.CharField(max_length=20, choices=PICKUP_CHOICES, default='8 A.M. to 9 A.M.')
    delivered_at = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=10, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking by {self.user} on {self.pickup_date}"