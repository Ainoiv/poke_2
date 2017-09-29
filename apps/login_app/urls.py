from django.conf.urls import url, include
from django.contrib import admin
from . import views
def test(request):
    print """

    I'm in the login app routing

    """

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),

]
