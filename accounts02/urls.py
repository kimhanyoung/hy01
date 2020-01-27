from django.urls import re_path
from accounts02 import views
from accounts02.views import *


app_name = 'accounts02'

urlpatterns = [

    re_path(r'^accounts02/$', AccountsListview.as_view(), name="list"),

]