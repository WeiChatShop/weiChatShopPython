from urllib import request
from django.db import connection,transaction
from weiChatShopPython.myapp.models import BookCart

__author__ = 'xiaoming'
#得到buid
def getBuid(request):
    buid = '1270001';
    if 'BUID' in request.COOKIES:
        buid = request.COOKIES['BUID'];
    return buid;
#得到用户的ip地址
def getRealIP(request):
    ip = '127.0.0.1'
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip =  request.META['REMOTE_ADDR']
    return ip;
#获得一本书的基本信息
def getOneBook(id):
    sqlForOneBook = "SELECT bi.`id`, bi.`name`, bi.`price`, bi.`freight`,bi.`path`,bi.`describe`,bi.prelist,bi.`list`,  bi.`stock`, " \
                " bi.`sell`, bi.`hot`, bi.`classify_id`,bc.id classify_id,bc.name classify_name "\
                "  FROM `book_info` bi left join book_class bc on(bi.classify_id=bc.id) where bi.status=1 and bi.id=%s ";
    cursor = connection.cursor();
    cursor.execute(sqlForOneBook,id);
    raw = cursor.fetchall();
    return raw;
#获得一个用户的基本信息
def getUserAddr(buid):
    sqlForAddr = "select * from user_info where uid=%s limit 1 ";
    cursor = connection.cursor();
    cursor.execute(sqlForAddr,buid);
    addr = cursor.fetchall();
    return addr;
#修改地址
def updateAddr(addr):
    updateAddrSQL = "update  `user_info` set `name`=%s,`phone`=%s,`province`=%s,"\
                "`city`=%s,`detail_addr`=%s,`addip`=%s,`require`=%s,`postalcode`=%s where uid=%s";
    try:
        with transaction.atomic():
            cursor = connection.cursor();
            cursor.execute(updateAddrSQL,[addr['name'],addr['phone'],addr['province'],
                                          addr['province'],addr['detail_addr'],addr['addip'],addr['require'],addr['postcode']
                                        ,addr['buid']]);
            transaction.commit_unless_managed();
            return True;
    except:
        return False;
def cartInsert(cartInfo):
    insertSQL = 'insert into book_cart(uid,addr_id,book_id,num,should_pay,addip,addtime)'\
                ' values(%s,%s,%s,%s,%s,%s,%s)'
    try:
        with transaction.atomic():
            cursor = connection.cursor();
            raw = cursor.execute(insertSQL,[cartInfo['buid'],cartInfo['addr_id'],cartInfo['book_id'],cartInfo['num'],
                                      cartInfo['total'],cartInfo['addip'],cartInfo['addtime']]);
            transaction.commit_unless_managed();
            return raw;
    except:
        return None;

def cartDataList(buid):
    cartListSQL = 'select bc.id,bc.uid,bc.book_id,bc.num,bc.should_pay,bi.price,bi.path,bi.name,bi.describe'\
                        ',bi.freight from book_cart bc left join book_info bi on bc.book_id=bi.id  where bc.uid=%s and bc.payment<=0'
    cursor = connection.cursor();
    cursor.execute(cartListSQL,[buid]);
    bookCart = cursor.fetchall();
    return bookCart;
def getCart(id,buid):
    getCartSQL = "select bc.id as cart_id ,bc.should_pay,bc.num,bi.price ," \
                "bc.addtime,bc.send_status,bi.freight,bi.name,bi.path,ui.name as realname," \
                "ui.id as ui_id,ui.phone,ui.province,ui.detail_addr from book_cart bc left join book_info bi " \
                "on bc.book_id=bi.id left join user_info ui on bc.uid=ui.uid where bc.id=%s and bc.uid=%s limit 1";
    cursor = connection.cursor();
    cursor.execute(getCartSQL,[id,buid]);
    bookCart = cursor.fetchall();
    return bookCart;