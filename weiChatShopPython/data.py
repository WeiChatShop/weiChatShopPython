# -*- coding: utf-8 -*-
__author__ = 'xiaoming'
from django.http import HttpResponse
from weiChatShopPython.myapp.models import BookInfo

def bookIndex(request):
    homeBookListSQL = "select `id`, `name`,`describe` ,path,hot, `classify_id`," \
                      "(select name from book_class bc where bi.classify_id=bc.id ) classify_name," \
                      "`price`, `freight`  from `book_info` bi where status=1";
    bookList = BookInfo.objects.raw(homeBookListSQL);
    return HttpResponse(bookList,content_type="application/json");

