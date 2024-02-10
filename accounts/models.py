from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES=(
        ('user','user'),
        ('moderator','moderator'),
        ('admin','admin')
    )

    email=models.EmailField(unique=True)
    role=models.CharField(max_length=30,choices=ROLES,default='user')
    description=models.TextField(blank=True,default='')

# Create your models here.

# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
