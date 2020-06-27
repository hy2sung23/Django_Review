from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    author = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, blank=True)
