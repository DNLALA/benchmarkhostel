from django.db import models
from users.models import User

class Hostel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'pending'),
        ('processing', 'processing'),
        ('successful', 'successful'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hostel', blank=True, null=True)
    room_type = models.CharField(max_length=100, blank=True, null=True)
    seater = models.CharField(max_length=100, blank=True, null=True)
    hostel = models.CharField(max_length=255, blank=True, null=True)
    issues = models.CharField(max_length=255, blank=True, null=True)
    issues_status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='pending')
    tranfar = models.BooleanField(default=False)
    tranfar_status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='pending')
    request = models.CharField(max_length=255, blank=True, null=True)
    request_status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS_CHOICES, default='pending')
    reports = models.CharField(max_length=255, blank=True, null=True)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    bed = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hostel} - {self.room_number}"
