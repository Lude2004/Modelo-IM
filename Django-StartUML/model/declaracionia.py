#-*- coding: utf-8 -*-

from django.db import models

class DeclaracionIA(models.Model):
    class Meta:
        pass

    fechaEmision = models.DateField()


    def generar_texto_declaracion(self, ):
        pass

    def generar_pdf(self, ):
        pass

