from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weiChatShopPython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$','weiChatShopPython.views.firstPage'),
    url(r'^index','weiChatShopPython.views.index'),
    url(r'^home','weiChatShopPython.views.home'),
    url(r'^now','weiChatShopPython.views.current_datetime'),
)
