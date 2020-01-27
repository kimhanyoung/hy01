from django.urls import re_path
from orders07 import views
from orders07.views import *


app_name = 'orders07'

urlpatterns = [

    re_path(r'^orders07/$', Orders07Listview.as_view(), name="list"),
    re_path(r'^(?P<pk>[0-9]+)/update/$', Orders07Updateview.as_view(), name="update"),
    re_path(r'^orders07/result/$', ResultListView.as_view(), name="return"),


]