from django.conf.urls import url

from .views import index, nueva, reporte_clientes,reporte_productos

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva/$', nueva, name='nueva'),
    url(r'^cliente/$', reporte_clientes, name='reporte_clientes'),
    url(r'^producto/$', reporte_productos, name='reporte_productos'),
]