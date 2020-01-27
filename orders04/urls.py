from django.urls import re_path
from orders04 import views
from orders04.views import *


app_name = 'orders04'

urlpatterns = [

    re_path(r'^orders04/$', Orders04CreateView.as_view(), name="input"),
    re_path(r'^orders04/result/$', PathmonthListView.as_view(), name="result"),   #경과월결과보여주기

]