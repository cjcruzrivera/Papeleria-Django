from django.conf.urls import url

from .views import index, ProductoCreateView, ProductoListView, ProductoUpdateView,eliminar

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', ProductoCreateView.as_view(), name='nuevo'),
    url(r'^listar/$', ProductoListView.as_view(), name='listar'),
    url(r'^editar/(?P<pk>\d+)/$', ProductoUpdateView.as_view(), name='editar'),
    url(r'^eliminar/$', eliminar, name='eliminar'),
]