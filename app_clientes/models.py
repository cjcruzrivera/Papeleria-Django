# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .validators import SEX_CHOICES, validateNumber
# Create your models here.

class Cliente(models.Model):
    identificacion = models.CharField(max_length=20)
    nombre = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    sexo = models.CharField(max_length=60, choices=SEX_CHOICES)
    telefono = models.CharField(max_length=60, validators=[validateNumber])
    fecha_nacimiento = models.DateField()