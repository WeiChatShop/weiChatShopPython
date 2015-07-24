# -*- coding: utf-8 -*-
__author__ = 'xiaoming'

from django.shortcuts import render, render_to_response
from django.template import loader,Context
from django.http import HttpResponse
from weiChatShopPython.myapp.models import BookInfo
import datetime;

def firstPage(request):
    return HttpResponse("<p>世界好</p>")
def index(request):
    indexSql = "select * from book_info";
    indexSet = BookInfo.objects.raw(indexSql);
    return render_to_response('home/pay.html',{'list':indexSet});
def home(request):
    book_list = BookInfo.objects.get(id=1);
    return HttpResponse("<p>"+''.join(book_list)+"</p>");
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)