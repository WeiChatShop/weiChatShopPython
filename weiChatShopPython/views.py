# -*- coding: utf-8 -*-
__author__ = 'xiaoming'

from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse

def firstPage(request):
    return HttpResponse("<p>世界好</p>")
def index(request):
    context          = {};
    context['label'] = 'Hello World!';
    return render(request, 'home/pay.html', context);
