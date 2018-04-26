from django.conf.urls import url

from .views import index, ClienteCreateView, ClienteListView

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo/$', ClienteCreateView.as_view(), name='nuevo'),
    url(r'^listar/$', ClienteListView.as_view(), name='listar'),
]