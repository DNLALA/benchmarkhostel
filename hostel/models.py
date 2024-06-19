from django.db import models
from users.models import User

class Hostel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='hostel')
    room_type = models.CharField(max_length=100)
    seater = models.CharField(max_length=100)
    hostel = models.CharField(max_length=255)
    room_number = models.CharField(max_length=50)
    bed = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.hostel} - {self.room_number}"
