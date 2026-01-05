#-*- coding: utf-8 -*-

from django.db import models

class Persona(models.Model):
    class Meta:
        pass

    nombre = models.CharField()
    apellido = models.CharField()
    rol = models.CharField()


