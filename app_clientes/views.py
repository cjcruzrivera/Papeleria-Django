# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

# Create your views here.
from .forms import ClienteForm
from .models import Cliente

def index(request):
    return render(request, 'cliente/index.html')


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('clientes:nuevo')

class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/cliente_list.html"

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "cliente/cliente_form.html"
    success_url = reverse_lazy('clientes:listar')
