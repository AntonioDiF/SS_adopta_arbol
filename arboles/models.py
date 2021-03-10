from django.db import models
from django.contrib.auth import get_user_model

from ubicaciones.models import Ubicacion

class ArbolEspecie(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ArbolUbicacion(models.Model):
    nombre = models.CharField(max_length=300)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class ArbolEstado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Arbol(models.Model):
    nombre = models.CharField(max_length=150)
    altura = models.FloatField()

    especie = models.ForeignKey(ArbolEspecie, on_delete=models.PROTECT)
    ubicacion = models.ForeignKey(ArbolUbicacion, on_delete=models.PROTECT)
    fecha_plantado = models.DateField(auto_now_add=True, blank=True, null=True)
    siembra_estado = models.ForeignKey(ArbolEstado, on_delete=models.PROTECT)
    pagado = models.BooleanField()

    plantado = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='arboles_plantados')
    cuidado = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='arboles_cuidados')

    def __str__(self):
        return self.nombre