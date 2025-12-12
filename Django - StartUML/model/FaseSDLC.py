#!/usr/bin/python
#-*- coding: utf-8 -*-

from enum import Enum

class FaseSDLC(Enum):
    PLANIFICACION = 1
    DISENO = 2
    IMPLEMENTACION = 3
    PRUEBAS = 4
    DESPLIEGUE = 5
    MANTENIMIENTO = 6
