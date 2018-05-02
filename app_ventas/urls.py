from django.conf.urls import url

from .views import index, nueva

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nueva/$', nueva, name='nueva'),
]