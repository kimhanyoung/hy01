from django.urls import re_path
from pentions import views
from pentions.views import *


app_name = 'pentions'
urlpatterns = [

    re_path(r'^$', PentionView.as_view(), name="index"),     #pention 첫화면

    # 5. 경험생명표별 연금액
    re_path(r'^ma500/$', Ma500CreateView.as_view(), name="ma500"),
    re_path(r'^ma500/result/$', Ma500ListView.as_view(), name="ma500result"),


]
