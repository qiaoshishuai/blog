#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 19:11
# @Author  : zhuhu
# @DES     : 
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
