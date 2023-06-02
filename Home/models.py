
from django.db import models

class cliente (models.Model):
    nombre = models.CharField(max_length=250, null=True, blank=True)
    apellido = models.CharField(max_length=250, null=True, blank=True)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    telefono = models.CharField(max_length=250, null=True, blank=True)
    estado = models.BooleanField(default=True)
    
class caso (models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    codigo_caso = models.CharField(max_length=250, null=True, blank=True)
    observacion = models.CharField(max_length=250, null=True, blank=True)
    departamento_actual = models.CharField(max_length=250, null=True, blank=True)
    usuario = models.CharField(max_length=250, null=True, blank=True)
    estado = models.BooleanField(default=True)
