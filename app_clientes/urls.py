from django.conf.urls import url

from .views import index, ClienteCreateView, ClienteListView, ClienteUpdateView, eliminar

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', ClienteCreateView.as_view(), name='nuevo'),
    url(r'^listar/$', ClienteListView.as_view(), name='listar'),
    url(r'^eliminar/$', eliminar, name='eliminar'),
    url(r'^editar/(?P<pk>\d+)/$', ClienteUpdateView.as_view(), name='editar'),
]