from django.urls import re_path
from orders05 import views
from orders05.views import *


app_name = 'orders05'

urlpatterns = [

    re_path(r'^orders05/$', Orders05CreateView.as_view(), name="input"),
    re_path(r'^orders05/result/$', InsuageListView.as_view(), name="result"),   #보험나이보여주기

]