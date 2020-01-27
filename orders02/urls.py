from django.urls import re_path
from orders02 import views
from orders02.views import *


app_name = 'orders02'

urlpatterns = [

    re_path(r'^orders02/$', Orders02CreateView.as_view(), name="input"),
    re_path(r'^orders02/result/$', ReturnmoneyListView.as_view(), name="return"),        #해지환급금 보여주기
    re_path(r'^orders02/pention/$', PentionListView.as_view(), name="pention"),          #연금액보여주기

]