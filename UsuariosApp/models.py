from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True) # designar usuario
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True) # designar imagen

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.avatar}"