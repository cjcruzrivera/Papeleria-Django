# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=150)
    precio_unitario = models.FloatField(max_digits=5,decimal_places=2)