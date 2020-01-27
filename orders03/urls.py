from django.urls import path, re_path
from orders03 import views
from orders03.views import *

app_name = 'orders03'

urlpatterns = [

    re_path(r'^orders03/$', Orders03CreateView.as_view(), name="input"),
    re_path(r'^orders03/change/$', FundchangeListView.as_view(), name="change"),        #펀드변경검증
    re_path(r'^fundchange/$', FundchangeCreateView.as_view(), name="statsinput"),
    re_path(r'^orders03/stats/$', ChangestatsListView.as_view(), name="stats"),          #펀드변경통계

]