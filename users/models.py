from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (
        ('regular', 'regular'),
        ('subsciber', 'subscriber'),
        ('moderator', 'moderator')
    )
    emial = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regualar')
    info = models.TextField('Description', max_length=600, default='', blank=True)

    def __str__(self):
        return self.username