# -*- coding: utf-8 -*-
from django.db.models.query import RawQuerySet

__author__ = 'xiaoming'

from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse
import datetime;

def firstPage(request):
    return HttpResponse("<p>世界好</p>")
# 跳转首页
def index(request):
    return render_to_response('home/index.html');
