from django.urls import re_path
from pentions import views
from pentions.views import *


app_name = 'pentions'
urlpatterns = [

    re_path(r'^$', PentionView.as_view(), name="index"),     #pention 첫화면


    #1. 투자의 원칙 (1)시간의 가치
    re_path(r'^ma100/$', Ma100CreateView.as_view(), name="ma100"),
    re_path(r'^ma100/result/$', Ma100ListView.as_view(), name="ma100result"),

    # 2. 투자의 원칙 (2)수익률
    re_path(r'^ma200/$', Ma200CreateView.as_view(), name="ma200"),
    re_path(r'^ma200/result/$', Ma200ListView.as_view(), name="ma200result"),

    # 3. 투자의 원칙 (3)세금
    re_path(r'^ma300/$', Ma300CreateView.as_view(), name="ma300"),
    re_path(r'^ma300/result/$', Ma300ListView.as_view(), name="ma300result"),

    # 4. 연금액계산
    re_path(r'^ma400/$', Ma400CreateView.as_view(), name="ma400"),
    re_path(r'^ma400/result/$', Ma400ListView.as_view(), name="ma400result"),

    # 5. 경험생명표별 연금액
    re_path(r'^ma500/$', Ma500CreateView.as_view(), name="ma500"),
    re_path(r'^ma500/result/$', Ma500ListView.as_view(), name="ma500result"),

    # 6. 연금예상액(즉시연금)
    re_path(r'^mc100/$', Mc100CreateView.as_view(), name="mc100"),
    re_path(r'^mc100/result/$', Mc100ListView.as_view(), name="mc100result"),

    # 7. 월목표연금액
    re_path(r'^mc200/$', Mc200CreateView.as_view(), name="mc200"),
    re_path(r'^mc200/result/$', Mc200ListView.as_view(), name="mc200result"),

    # 8. 연금개시후 공시이율
    re_path(r'^mc300/$', Mc300CreateView.as_view(), name="mc300"),
    re_path(r'^mc300/result/$', Mc300ListView.as_view(), name="mc300result"),

    # 9. 변액연금비용
    re_path(r'^md100/$', Md100CreateView.as_view(), name="md100"),
    re_path(r'^md100/result/$', Md100ListView.as_view(), name="md100result"),

    # . 위험보험료
    re_path(r'^md200/$', Md200CreateView.as_view(), name="md200"),
    re_path(r'^md200/result/$', Md200ListView.as_view(), name="md200result"),

    # 적금의 비밀
    re_path(r'^mg100/$', Mg100CreateView.as_view(), name="mg100"),
    re_path(r'^mg100/result/$', Mg100ListView.as_view(), name="mg100result"),

    # 수익률별 연금예상액
    re_path(r'^mh200/$', Mh200CreateView.as_view(), name="mh200"),
    re_path(r'^mh200/result/$', Mh200ListView.as_view(), name="mh200result"),

]
