from django.db import models

class Region(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre

class Ubicacion(models.Model):
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    coordX = models.FloatField()
    coordY = models.FloatField()

    def __str__(self):
        return f"{self.coordX}, {self.coordY}"