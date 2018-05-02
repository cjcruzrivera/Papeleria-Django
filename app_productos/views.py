# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, Http404



from .models import Producto
from .forms import ProductoForm

# Create your views here.


def index(request):
    return render(request, 'producto/index.html')

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto_form.html"
    success_url = reverse_lazy('productos:listar')

class ProductoListView(ListView):
    model = Producto
    template_name = "producto/producto_list.html"

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto_form.html"
    success_url = reverse_lazy('productos:listar')

def eliminar(request):
    pk = request.POST.get('id_producto')
    if not pk:
        raise Http404
    producto_borrar = Producto.objects.get(pk=pk)
    producto_borrar.delete()
    response = {'exito':'ok'}
    return JsonResponse(response)