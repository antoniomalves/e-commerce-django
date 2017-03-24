# coding=utf-8

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.list_produtos, name='list_produtos'),
    url(r'^(?P<slug>[\w_-]+)/$', views.categoria, name='categoria'),
    url(r'^produtos/(?P<slug>[\w_-]+)/$', views.produto, name='produto'),
]