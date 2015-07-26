# -*- coding: utf-8 -*-
from django.core import serializers
import simplejson
from weiChatShopPython.service import updateAddr, getRealIP, getBuid

__author__ = 'xiaoming'
from django.http import HttpResponse
from django.template import loader,Context
from weiChatShopPython.myapp.models import BookInfo
from django.db import connection,transaction;
#首页图书轮播图
def bookIndex(request):
    # homeBookListSQL = "select `id`, `name`,`describe` ,path,hot, `classify_id`, `price`, `freight`  from `book_info` as bi where status=1";
    bookList = BookInfo.objects.filter(status=1);
    return HttpResponse(serializers.serialize("json",bookList,ensure_ascii = False),content_type="application/json");
def classify(request,id):
    sqlForBookList =\
                "select bi.`id`, bi.`name`,bi.`describe` ,bi.path,bi.hot, bi.`classify_id`,bc.name classifyname,bc.describe classifydesc,"\
                " bi.`price`, bi.`freight`  from `book_info` bi left join book_class bc on(bi.classify_id=bc.id) where bi.status=1 and bi.classify_id=%s";
    cursor = connection.cursor();
    cursor.execute(sqlForBookList,id);
    raw = cursor.fetchall();
    return HttpResponse(simplejson.dumps({'status': '1', 'message':'chenggong','data':raw},ensure_ascii=False), content_type='application/json');
def editAddr(request):
    buid = getBuid(request);
    addr = {};
    addr['name'] = request.GET['name']
    addr['phone'] = request.GET['phone']
    addr['province'] = request.GET['province']
    addr['detail_addr'] = request.GET['detail_addr']
    addr['addip'] = getRealIP(request);
    addr['postcode'] = request.GET['postCode']
    addr['require'] = request.GET['require']
    addr['book_id'] = request.GET['book_id']
    addr['buid'] = buid;
    status = updateAddr(addr);
    if status :
        return HttpResponse(simplejson.dumps({'status': '1', 'message':'success','data':""},ensure_ascii=False), content_type='application/json');
    else :
        HttpResponse(simplejson.dumps({'status': '0', 'message':'修改失败!','data':""},ensure_ascii=False), content_type='application/json');