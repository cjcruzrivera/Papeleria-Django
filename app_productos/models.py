# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=150)
    precio_unitario = models.IntegerField(validators=[MinValueValidator(0)])

    def __unicode__(self):
        return '{}'.format(self.nombre)

