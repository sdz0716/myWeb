from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ip>[0-9]+)/$', views.ipinfo, name='ipinfo'),
    url(r'^(?P<ip>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^list/$', views.serverlist, name='serverlist'),
]