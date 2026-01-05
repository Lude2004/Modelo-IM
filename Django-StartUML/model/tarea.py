#-*- coding: utf-8 -*-

from django.db import models

class Tarea(models.Model):
    class Meta:
        pass

    nombre = models.CharField()
    descripcion = models.CharField()
    seleccionada = models.BooleanField()


    def asignar_herramienta(self, ):
        pass

