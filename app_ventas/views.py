# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from app_clientes.models import Cliente
from app_productos.models import Producto
# Create your views here.

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/index.html',{
        'clientes':clientes
    })
