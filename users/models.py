from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from datetime import datetime
from rest_framework.authtoken.models import Token
import uuid
from django.utils import timezone

class CustomUserManager(UserManager):
    """Custom manager for User model with no username field."""

    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('Email is required')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False
    )
    username = models.CharField(max_length=255, unique=True)
    reg_no = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_warden = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def tokens(self):
        token, _ = Token.objects.get_or_create(user=self)
        return token.key
