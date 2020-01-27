from django.urls import re_path
from pentionsto import views
from pentionsto.views import *


app_name = 'pentionsto'
urlpatterns = [

    # 4. 연금액계산(변액)
    re_path(r'^ma400/$', Ma400CreateView.as_view(), name="ma400"),
    re_path(r'^ma400/result/$', Ma400ListView.as_view(), name="ma400result"),

    # 4. 연금액계산(공시)
    re_path(r'^ma600/$', Ma600CreateView.as_view(), name="ma600"),
    re_path(r'^ma600/result/$', Ma600ListView.as_view(), name="ma600result"),


]
