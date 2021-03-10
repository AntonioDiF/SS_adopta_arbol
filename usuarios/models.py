from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=300, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=300, blank=True, null=True)
    apellido_materno = models.CharField(max_length=300, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.username