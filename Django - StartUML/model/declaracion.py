#-*- coding: utf-8 -*-

from django.db import models

class Declaracion(models.Model):
    class Meta:
        pass

    fechaCreacion = models.DateField()


    def generarTextoDeclaracion(self, ):
        pass

    def exportarDeclaracion(self, ):
        pass

