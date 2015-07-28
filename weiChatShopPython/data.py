# -*- coding: utf-8 -*-
import datetime
from django.core import serializers
import simplejson
from weiChatShopPython.service import updateAddr, getRealIP, getBuid, cartInsert, cartDataList, addrInsert

__author__ = 'xiaoming'
from django.http import HttpResponse
from django.template import loader,Context
from weiChatShopPython.myapp.models import BookInfo, BookCart
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
    addr['name'] = request.REQUEST.get('name','zmw');
    addr['phone'] = request.REQUEST.get('phone','15313306298');
    addr['province'] = request.REQUEST.get('province','北京');
    addr['detail_addr'] = request.REQUEST.get('detail_addr');
    addr['addip'] = getRealIP(request);
    addr['postcode'] = request.REQUEST.get('postCode','18888');
    addr['require'] = request.REQUEST.get('require','没有');
    addr['book_id'] = request.REQUEST.get('book_id',"1");
    addr['buid'] = buid;
    status = updateAddr(addr);
    if status :
        return HttpResponse(simplejson.dumps({'status': '1', 'message':'success','data':""},ensure_ascii=False), content_type='application/json');
    else :
        HttpResponse(simplejson.dumps({'status': '0', 'message':'修改失败!','data':""},ensure_ascii=False), content_type='application/json');

#有地址的购买
def buyWithAddrExist(request):
    cartInfo = {};
    cartInfo['addr_id'] = request.REQUEST.get('addr_id',0);
    cartInfo['book_id'] = request.REQUEST.get('book_id',1);
    cartInfo['num'] = request.REQUEST.get('num',1);
    cartInfo['total'] = request.REQUEST.get('total',0);
    cartInfo['addip'] = getRealIP(request);
    cartInfo['addtime'] = datetime.datetime.now();
    cartInfo['buid'] =  getBuid(request);
    id = cartInsert(cartInfo);
    if id is None:
        return HttpResponse(simplejson.dumps({'status': '0', 'message':'加入购物车失败!','data':""},
                                             ensure_ascii=False), content_type='application/json');
    else:
        return HttpResponse(simplejson.dumps({'status': '1', 'message':'修改成功!','data':id},
                                      ensure_ascii=False), content_type='application/json');
#回到购物车列表
def cartList(request):
    buid = getBuid(request);
    bookCartList = cartDataList(buid);
    if bookCartList is not None:
        return HttpResponse(simplejson.dumps({'status': '1', 'message':'有未付款的购物','data':bookCartList},
                                      ensure_ascii=False), content_type='application/json');
    else:
        return HttpResponse(simplejson.dumps({'status': '0', 'message':'请您先去购物吧!','data':bookCartList},
                                  ensure_ascii=False), content_type='application/json');
def buyIt(request):
    buid = getBuid(request);
    addtime = datetime.datetime.now();
    IP = getRealIP(request);
    cartInfo = {};
    cartInfo['addr_id'] = request.REQUEST.get('addr_id',0);
    cartInfo['book_id'] = request.REQUEST.get('book_id',1);
    cartInfo['num'] = request.REQUEST.get('num',1);
    cartInfo['total'] = request.REQUEST.get('total',0);
    cartInfo['addip'] = IP;
    cartInfo['addtime'] = addtime;
    cartInfo['buid'] = buid;
    addrInfo = {};
    addrInfo['buid'] = buid;
    addrInfo['name'] = request.REQUEST.get('name',0);
    addrInfo['phone'] = request.REQUEST.get('phone',0);
    addrInfo['province']= request.REQUEST.get('province',0);
    addrInfo['city']= request.REQUEST.get('province',0);
    addrInfo['detail_addr']= request.REQUEST.get('detail_addr',0);
    addrInfo['addip']= IP;
    addrInfo['addtime'] = addtime;
    addrInfo['require']= request.REQUEST.get('require',0);
    addrInfo['postalcode']= request.REQUEST.get('postCode',0);
    addrInsert(addrInfo);
    status = cartInsert(cartInfo);
    if status is None:
        return HttpResponse(simplejson.dumps({'status': '0', 'message':'购买失败!','data':""},
                                  ensure_ascii=False), content_type='application/json');
    return HttpResponse(simplejson.dumps({'status': '1', 'message':'成功!','data':""},
                                  ensure_ascii=False), content_type='application/json');