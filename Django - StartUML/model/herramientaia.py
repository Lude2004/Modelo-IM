#-*- coding: utf-8 -*-

from django.db import models

class HerramientaIA(models.Model):
    class Meta:
        pass

    nombre = models.CharField()
    version = models.CharField()


