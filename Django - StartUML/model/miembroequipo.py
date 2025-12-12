#-*- coding: utf-8 -*-

from django.db import models

class MiembroEquipo(models.Model):
    class Meta:
        pass

    nombre = models.CharField()
    rol = models.CharField()


