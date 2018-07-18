#from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    # index
    re_path(r'^$', views.index, name='index'),

    # monitor
    re_path(r'^monitor/$', views.monitor, name='monitor'),
    re_path(r'^monitor/(?P<controller_name>[^/]+)/(?P<desc>[^/]+)/(?P<timerange>[1-4])/(?P<plotnumber>[1-6])/$', views.scopedraw, name='scopedraw'),

    # detail
    re_path(r'^detail/(?P<controller_name>[^/]+)/$', views.detail, name='detail'),

    # get data
    re_path(r'^data/(P?<controller_name>[^/]+)/(?P<desc>[^/]+)/(?P<time_start_str>[^/]+)/(?P<time_end_str>[^/]+)/$', views.getData, name='getdata')



]
