from django.urls import path, re_path
from orders import views
from .views import *

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),


#3. 적립식펀드
    re_path(r'^fund/$', FundCreateView.as_view(), name="fund"),
    re_path(r'^fund/result/$', FundListView.as_view(), name="fundresult"),

#변액
    re_path(r'^variable/basic/$', BasicListView.as_view(), name="basic"),          #펀드그래프화면
    re_path(r'^(?P<result_id>\d+)/fund/new/$', views.fund_new, name="fund_new"),  #펀드현황 상세화면 생성
    re_path(r'^variable/detail/$', FunddetailView.as_view(), name="fund_detail"),          #펀드그래프화면 보여주기
    re_path(r'^variable/earning/$', EearningListView.as_view(), name="earning"),          #수익률화면보여주기
    re_path(r'^variable/return/$', ReturnmoneyListView.as_view(), name="return"),          #해지환급금보여주기
    re_path(r'^variable/pention/$', PentionListView.as_view(), name="pention"),          #연금액보여주기
]

