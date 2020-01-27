from django.urls import re_path                 #기존의 url 과 동일
from funds import views
from funds.views import *


app_name = 'funds'                                   #장고 2.0 이후 프로잭트 url.py에 namespace 없애고 추가된 내용
urlpatterns = [

    re_path(r'^$', FundView.as_view(), name="index"),     #fund 첫화면


    # 1. 펀드검색
    re_path(r'^search/$', SearchFormView.as_view(), name='search'),
                                             # Example: /99/update/
    re_path(r'^(?P<pk>[0-9]+)/update/$',FundUpdateView.as_view(), name="update"),

    re_path(r'^fa100/$', Fa100CreateView.as_view(), name="fa100"),
    re_path(r'^fa100/result/$', Fa100ListView.as_view(), name="fa100result"),

]