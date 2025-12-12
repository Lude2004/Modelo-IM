#-*- coding: utf-8 -*-

from django.db import models

class Proyecto(models.Model):
    class Meta:
        pass

    titulo = models.CharField()
    metodologia = models.CharField()


