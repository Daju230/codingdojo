from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs$', views.index),
    url(r'^blogs/new/$', views.new),
    url(r'^blogs/create$', views.create),
    url(r'^/(?P<number>\d+)$', views.show),
    url(r'^/(?P<number>\d+)/edit$', views.edit),
    url(r'^/(?P<number>\d+)/delete$', views.destroy)
]