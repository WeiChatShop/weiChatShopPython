from django.conf.urls import patterns, include, url
from django.contrib import admin
import weiChatShopPython

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weiChatShopPython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','weiChatShopPython.views.firstPage'),
    url(r'^index','weiChatShopPython.views.index'),
    url(r'^home','weiChatShopPython.views.home'),
    url(r'^bookindex$','weiChatShopPython.data.bookIndex',name='ajax-dict'),
    url(r'^one/(\d{1})$','weiChatShopPython.views.oneBook'),
    url(r'^classify/(\d{1})$','weiChatShopPython.data.classify'),
    url(r'^editcart$','weiChatShopPython.data.editAddr'),
    url(r'^buyitaddr','weiChatShopPython.data.buyWithAddrExist'),
    url(r'^buynow/(\d{1})$','weiChatShopPython.views.buynow'),
    url(r'^pay$','weiChatShopPython.views.payView'),
    url(r'^cart$','weiChatShopPython.views.cartList'),
    url(r'^getCartData$','weiChatShopPython.data.cartList'),
    url(r'^buyit','weiChatShopPython.data.buyIt'),
    url(r'^classify$','weiChatShopPython.views.classify'),
    url(r'^hotBook','weiChatShopPython.views.oneHotBook'),
    url(r'^now','weiChatShopPython.views.current_datetime'),
      (r'^site_medias/(?P<path>.*)$','django.views.static.serve',
        {'document_root':weiChatShopPython.settings.STATICFILES_DIRS, 'show_indexes': True}),
)
