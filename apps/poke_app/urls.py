from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^addpoke/(?P<id>\d+)$', views.addpoke),
]
