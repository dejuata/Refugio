from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domicilio = models.TextField()
    
    # Funcion para devolver la etiqueta del nombre del objeto
    def __str__(self):
		return '{} {}'.format(self.nombre, self.apellidos)
    

