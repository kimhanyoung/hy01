from django.urls import re_path
from vund import views
from vund.views import *


app_name = 'vund'
urlpatterns = [

    re_path(r'^$', VundView.as_view(), name="index"),     #fund 첫화면


    # 1. 펀드검색
    re_path(r'^search/$', SearchFormView.as_view(), name='search'),
                                                          # Example: vund/99/update/
    re_path(r'^vund/(?P<pk>[0-9]+)/update/$',VundUV.as_view(), name="vund_update"),

                 #  펀드명별도실습  url(r'^ma100/$', Ma100UpdateView.as_view(), name="ma100"),




]