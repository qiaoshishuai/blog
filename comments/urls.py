#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 14:19
# @Author  : zhuhu
# @DES     :
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

app_name = 'comment'
urlpatterns = [
    url(r'^post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]
