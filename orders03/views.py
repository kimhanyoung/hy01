from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView, CreateView
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from datetime import date
from django.urls import reverse_lazy
from .models import *
from mysite.views import LoginRequiredMixin


class Orders03CreateView(LoginRequiredMixin, CreateView) :
    model = Ae00Input
    fields = ['classification','start_date','end_date']
    success_url = reverse_lazy('orders03:change')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Orders03CreateView, self).form_valid(form)


# 펀드변경 검증화면 보여주기
class FundchangeListView(ListView):
    template_name = 'orders03/ae01fundchange.html'
    context_object_name = 'object_list'
    queryset = Ae05Result.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FundchangeListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ae10Graph.objects.filter(user=user),        # or with some filter appli
            'object_list02': Ae01Out.objects.filter(user=user),       # or with some filter appli
            'object_list03': Ae11Startend.objects.filter(user=user),  # or with some filter appli
            'object_list04': Ae13Count.objects.filter(user=user),  # or with some filter appli
            'object_list05': Ag00Fundalarm.objects.order_by('-date'),  # or with some filter appli
            'object_list06': Ae05Result.objects.filter(user=user),  # or with some filter appli
            'object_list07': Ae05Result01.objects.filter(user=user),  # or with some filter appli

        })
        return context

# 펀드변경 통계 입력용
class FundchangeCreateView(LoginRequiredMixin, CreateView) :
    model = Af01input
    template_name = 'orders03/af01fundchange.html'
    fields = ['path_month']

    success_url = reverse_lazy('orders03:stats')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FundchangeCreateView, self).form_valid(form)


# 펀드변경 통계 보여주기
class ChangestatsListView(ListView):
    template_name = 'orders03/ae02stats.html'
    context_object_name = 'object_list'
    queryset = Af07Result.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ChangestatsListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Af14Graph.objects.filter(user=user),      # or with some filter appli
            'object_list02': Af07Result.objects.filter(user=user)

        })
        return context


