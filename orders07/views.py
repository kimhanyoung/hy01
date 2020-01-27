from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from chartit import DataPool, Chart
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from mysite.views import LoginRequiredMixin
from orders.models import *
from orders07.models import *
from orders07.views import *
from django.contrib import messages


class Orders07Listview(LoginRequiredMixin, ListView):
    template_name = 'orders07/metfund_list.html'

    def get_queryset(self):
        return Metfund.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Orders07Listview, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Aa01Totalcount.objects.filter(user=user),  #
            'object_list02': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
            'object_list03': Metfund.objects.filter(user=user),
        })
        return context


class Orders07Updateview(LoginRequiredMixin, PermissionRequiredMixin, UpdateView) :
    permission_required = 'orders07.change_metfund'
    model = Metfund
    fields = ['fund_name','count']
    success_url = reverse_lazy('orders07:list')

    def get_login_url(self):                  # PermissionRequiredMixin 에 의거 다이렉트
        return 'accounts02:list'


class ResultListView(ListView):
    template_name = 'orders07/metfund_return.html'
    context_object_name = 'object_list'
    queryset = Aa02Enterout.objects.all()

    def get_context_data(self, **kwargs):
        context = super( ResultListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
            'object_list00': Ac04Pentionout.objects.filter(user=user),
            'object_list20': Ab06Presentpayment.objects.filter(user=user),  #
            'object_list21': Ac02Returnmoneyout.objects.filter(user=user).filter(
                Q(path_month='3') | Q(path_month='6') | Q(path_month='9') | Q(path_month='12') | Q(path_month='24') | Q(
                    path_month='36') | Q(path_month='48') | Q(path_month='60') | Q(path_month='72') | Q(
                    path_month='84') | Q(path_month='96') | Q(path_month='108') | Q(path_month='120') | Q(
                    path_month='180') | Q(path_month='240') | Q(path_month='300') | Q(path_month='360') | Q(
                    path_month='420') | Q(path_month='480')),
            'object_list31': Aa07Presentpayment.objects.filter(user=user),   # 펀드선택(BM) 현재투자결과
            'object_list32': Aa08Expectrate.objects.filter(user=user),   # 펀드선택(BM) 예상수익률
            'object_list33': Aa12Pentionout.objects.filter(user=user),     # 펀드선택(BM) 예상연금액

            'object_list61': Ac03Fundrate.objects.filter(user=user),  # 원래 가입한 펀드수익률
            'object_list62': Ac06Metrate.objects.filter(user=user),  # 펀드선택(BM) 펀드수익률
            'object_list70': Aa33Kospirate.objects.filter(user=user),  # kospi 수익률

            'object_list41': Ab02fundprice.objects.filter(user=user).filter(Q(count='1')),  # 펀드선택(BM) 1펀드그래프
            'object_list42': Ab02fundprice.objects.filter(user=user).filter(Q(count='2')),  # 펀드선택(BM) 2펀드그래프
            'object_list43': Ab02fundprice.objects.filter(user=user).filter(Q(count='3')),  # 펀드선택(BM) 3펀드그래프
            'object_list44': Ab02fundprice.objects.filter(user=user).filter(Q(count='4')),  # 펀드선택(BM) 4펀드그래프
            'object_list45': Ab02fundprice.objects.filter(user=user).filter(Q(count='5')),  # 펀드선택(BM) 5펀드그래프
            'object_list46': Ab02fundprice.objects.filter(user=user).filter(Q(count='6')),  # 펀드선택(BM) 6펀드그래프
            'object_list47': Ab02fundprice.objects.filter(user=user).filter(Q(count='7')),  # 펀드선택(BM) 7펀드그래프
            'object_list48': Ab02fundprice.objects.filter(user=user).filter(Q(count='8')),  # 펀드선택(BM) 8펀드그래프
            'object_list49': Ab02fundprice.objects.filter(user=user).filter(Q(count='9')),  # 펀드선택(BM) 9펀드그래프'
            'object_list51': Ab04entrygraph.objects.filter(user=user),  # 펀드선택(BM) 가입일그래프
            'object_list52': Ab03kospigraph.objects.all(),  # kospi

        })
        return context





