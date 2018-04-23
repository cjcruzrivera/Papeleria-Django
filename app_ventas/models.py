# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from app_clientes.models import Cliente
from app_productos.models import Producto
# Create your models here.

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente)
    producto = models.ForeignKey(Producto)
    total = models.IntegerField()