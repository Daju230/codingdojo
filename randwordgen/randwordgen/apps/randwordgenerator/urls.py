from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^clear/sessions', views.clear_session),
	url(r'^create', views.create),
]