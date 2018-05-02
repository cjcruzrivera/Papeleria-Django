# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.core import serializers

from app_clientes.models import Cliente
from app_productos.models import Producto
from app_ventas.models import Venta

# Create your views here.

def index(request):
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    ventas = Venta.objects.all()
    for venta in ventas:
        venta.total_ventas=venta.total*venta.producto.precio_unitario
        
    return render(request, 'ventas/index.html',{
        'clientes':clientes,
        'productos':productos,
        'ventas':ventas,
    })

def nueva(request):
    cliente_id = request.POST.get('id_cliente')
    if not cliente_id:
        raise Http404
    producto_id = request.POST.get('id_producto')
    cliente = Cliente.objects.get(pk=cliente_id)
    producto = Producto.objects.get(pk=producto_id)
    venta = Venta(cliente=cliente, producto=producto,total=request.POST.get('total'))
    venta.save()
    response = {'exito':'ok'}
    return JsonResponse(response)

def reporte_clientes(request):
    cliente_id = request.POST.get('id_cliente')
    if not cliente_id:
        raise Http404
    cliente = Cliente.objects.get(pk=cliente_id)
    queryset_ventas = Venta.objects.filter(cliente=cliente)
    ventas = []

    for q_venta in queryset_ventas:
        venta = {
            'id': q_venta.id,
            'cliente': q_venta.cliente.nombre + ' ' + q_venta.cliente.apellidos,
            'producto': q_venta.producto.nombre,
            'cantidad': q_venta.total,
            'total': q_venta.total*q_venta.producto.precio_unitario
        }
        ventas.append(venta)
    # ventas_json = serializers.serialize('json', ventas)
    response = {'exito':'ok', 'ventas': ventas}
    return JsonResponse(response)


def reporte_productos(request):
    producto_id = request.POST.get('id_producto')
    if not producto_id:
        raise Http404
    producto = Producto.objects.get(pk=producto_id)
    queryset_ventas = Venta.objects.filter(producto=producto)
    ventas = []

    for q_venta in queryset_ventas:
        venta = {
            'id': q_venta.id,
            'cliente': q_venta.cliente.nombre + ' ' + q_venta.cliente.apellidos,
            'producto': q_venta.producto.nombre,
            'cantidad': q_venta.total,
            'total': q_venta.total*q_venta.producto.precio_unitario
        }
        ventas.append(venta)
    # ventas_json = serializers.serialize('json', ventas)
    response = {'exito':'ok', 'ventas': ventas}
    return JsonResponse(response)