from django.views.generic import ListView
from chartit import DataPool, Chart
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from datetime import datetime
from datetime import date

from mysite.views import LoginRequiredMixin
from orders02.models import *
from orders02.views import *



class Orders02CreateView(LoginRequiredMixin, CreateView) :
    model = Ad00Input
    fields = ['count','payment']
    #fields = '__all__'
    success_url = reverse_lazy('orders02:return')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Orders02CreateView, self).form_valid(form)

class ReturnmoneyListView(ListView):
    template_name = 'orders02/ad01returnmoney.html'
    context_object_name = 'object_list'
    queryset = Ad03Returnmoneyout.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ReturnmoneyListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ad03Returnmoneyout.objects.filter(user=user).filter(Q(path_month='3')|Q(path_month='6')|Q(path_month='9')|Q(path_month='12')|Q(path_month='24')|Q(path_month='36')|Q(path_month='48')|Q(path_month='60')|Q(path_month='72')|Q(path_month='84')|Q(path_month='96')|Q(path_month='108')|Q(path_month='120')|Q(path_month='180')|Q(path_month='240')|Q(path_month='300')|Q(path_month='360')|Q(path_month='420')|Q(path_month='480')),
            'object_list20': Ad06Enterout.objects.filter(user=user)

        })
        return context


# 예상연금액보여주기
class PentionListView(ListView):
    template_name = 'orders02/ad02pention.html'
    context_object_name = 'object_list'
    queryset = Ad05Pentionout.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PentionListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ad04Pentionmoney.objects.filter(user=user),       # or with some filter appli
            'object_list02': Ad03Returnmoneyout.objects.filter(user=user),  # or with some filter appli
            'object_list03': Ad05Pentionout.objects.filter(user=user),
        })
        return context
