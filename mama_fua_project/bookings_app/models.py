from django.conf import settings
from django.db import models

# Create your models here.
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('ready for pick up', 'Ready for pickup'),
        ('transaction complete', 'Transaction completed')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    picked_at = models.DateTimeField(null=True,blank=True)
    delivered_at = models.DateTimeField(null=True,blank=True)
    location = models.CharField(max_length=10,null=True,blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title