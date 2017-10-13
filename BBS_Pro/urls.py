from django.conf.urls import patterns, include, url
from django.contrib import admin
import app01.urls
from app01.views import login,logout,readexcel,subexcel,info_search,info_wr
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'',include(app01.urls)),
    url(r'^login/$',login),
    url(r'^logout/$',logout),
    url(r'^readexcel',readexcel),
    url(r'^subexcel',subexcel),
    url(r'^info_search/$',info_search),
    url(r'^info_wr/$',info_wr),
)
