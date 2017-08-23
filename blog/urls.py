#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 14:19
# @Author  : zhuhu
# @DES     : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    url(r'^category/(?P<pk>[0-9]+)$', views.category, name='category'),
    url(r'^tag/(?P<pk>[0-9]+)$', views.tag, name='tag'),
    url(r'^archieves/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archieves, name='archieves'),
]
