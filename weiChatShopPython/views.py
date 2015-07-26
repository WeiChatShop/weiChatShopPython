# -*- coding: utf-8 -*-
from urllib import request
from weiChatShopPython.service import getOneBook, getUserAddr, getBuid

__author__ = 'xiaoming'

from django.shortcuts import render, render_to_response
from django.template import loader, Context
from django.http import HttpResponse
from weiChatShopPython.myapp.models import BookInfo


def firstPage(request):
    return HttpResponse("<p>世界好</p>")


# 跳转首页
def index(request):
    return render(request, 'home/index.html');


def oneBook(request, id):
    sqlForOneBook = "SELECT bi.`id`, bi.`name`, bi.`price`, bi.`freight`,bi.`describe`,bi.prelist,bi.`list`, bi.`path`, bi.`stock`, " \
                    " bi.`sell`, bi.`hot`, bi.`classify_id`,bc.id classify_id,bc.name classify_name " \
                    "  FROM `book_info` bi left join book_class bc on(bi.classify_id=bc.id) where bi.status=1 and bi.id=%s ";
    onebook = BookInfo.objects.raw(sqlForOneBook, [id]);
    for book in onebook:
        return render_to_response('home/oneBook.html', {'oneBook': book});


def classify(request):
    return render(request, 'home/classify.html')


def buynow(request, id):
    buid = getBuid(request);
    oneBook = getOneBook(id);
    addr = getUserAddr(buid)
    if addr is None:
        return render_to_response('cart/buy.html',
                                  {'id': oneBook[0][0], 'path': oneBook[0][4], 'name': oneBook[0][1], 'price': oneBook[0][2],
                                   'carriage': oneBook[0][3]})
    return render_to_response('cart/buyaddr.html',
           {'id': oneBook[0][0], 'path': oneBook[0][4], 'name': oneBook[0][1], 'price': oneBook[0][2],
             'carriage': oneBook[0][3], 'addrid':addr[0][0],'username':addr[0][2],
             'phone':addr[0][3],'province':addr[0][4],'detail_addr':addr[0][6],
             'postalcode':addr[0][7],'require':addr[0][8]});



