#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 18:00
# @Author  : zhuhu
# @DES     : 
# @File    : blog_tags.py
# @Software: PyCharm

from ..models import Post, Category, Tag
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.all().dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories(num=20):
    return Category.objects.all()[:num]


@register.simple_tag
def get_tags():
    return Tag.objects.all()
