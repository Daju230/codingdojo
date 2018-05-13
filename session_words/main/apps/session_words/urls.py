from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^localhost/session_words$', views.index),
    url(r'^localhost/session_words/add_word$', views.add_word),
    url(r'^localhost/session_words/clear$', views.clear)
]