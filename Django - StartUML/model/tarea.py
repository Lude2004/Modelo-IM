#-*- coding: utf-8 -*-

from django.db import models

class Tarea(models.Model):
    class Meta:
        pass

    nombre = models.CharField()
    descripcion = models.CharField()


