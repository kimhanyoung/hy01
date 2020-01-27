from django.urls import re_path
from orders06 import views
from orders06.views import *


app_name = 'orders06'
urlpatterns = [

# . 흥부와 놀부 -----둘다 listview
    re_path(r'^hungbu/$', HungbuListView.as_view(), name="hungbu"),
    re_path(r'^hungbu/result/$', HungbuListView02.as_view(), name="hungburesult"),

]