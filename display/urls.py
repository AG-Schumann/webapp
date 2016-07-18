from django.conf.urls import url

from . import views

urlpatterns = [
    # index
    url(r'^$', views.index, name='index'),

    # monitor
    url(r'^monitor/$', views.monitor, name='monitor'),
    url(r'^monitor/(?P<controller>.+)/(?P<select>.+)/(?P<timerange>.+)/(?P<plotnumber>.+)/$', views.scopedraw, name='scopedraw'),

    # detail
    url(r'^detail/(?P<config_controller>.+)/$', views.detail, name='detail'),
    #url(r'^(?P<controller>.+)/(?P<select>.+)/(?P<t1>.+)/(?P<t2>.+)/(?P<t3>.+)/(?P<t4>.+)/(?P<t5>.+)/$', views.getCVSdata, name='getCVSdata'),
    url(r'^data/(?P<controller>.+)/(?P<select>.+)/(?P<t1>.+)/(?P<t2>.+)/(?P<t3>.+)/(?P<t4>.+)/(?P<t5>.+)/$', views.getCVSdata, name='getCVSdata'),



]
