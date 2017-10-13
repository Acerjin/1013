'''
Created on 2016-1-16

@author: Administrator
'''
from django.conf.urls import patterns, include
import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^pub_bbs/new_bbs/$',views.new_bbs),
    (r'^comments/', include('django_comments.urls')),
    (r'^nj/$',views.index1),
    (r'^bbs/(\d+)/$',views.bbs),
    (r'^sub_comment/$',views.sub_comment),
    (r'^(\d+)/$',views.index_category),
    (r'^pub_bbs/$',views.pub_bbs),
    (r'^http/$',views.httpview),
    (r'^bbsview/$',views.bbsview),
    (r'^index/$',views.index),
                       
    
)
