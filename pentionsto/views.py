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
from pentionsto.models import *
from pentionsto.views import *


# 4. 연금액계산 (변액)
class Ma400CreateView(LoginRequiredMixin, CreateView) :
    model = Ma400In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'earning_rate','pention_start_rate']
    success_url = reverse_lazy('pentionsto:ma400result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma400CreateView, self).form_valid(form)


class Ma400ListView(LoginRequiredMixin, ListView):
    template_name = 'pentionsto/ma400_result.html'
    context_object_name = 'object_list00'
    queryset = Ma400Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Ma400ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list': Ma400Out.objects.filter(user=user),  #
            'object_list01': Ma400Out01.objects.filter(user=user),  # 해지환급금

        })
        return context

# 5. 연금액계산 (공시이율)
class Ma600CreateView(LoginRequiredMixin, CreateView) :
    model = Ma600In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'public_rate','pention_start_rate']
    success_url = reverse_lazy('pentionsto:ma600result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma600CreateView, self).form_valid(form)


class Ma600ListView(LoginRequiredMixin, ListView):
    template_name = 'pentionsto/ma600_result.html'
    context_object_name = 'object_list00'
    queryset = Ma600Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Ma600ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list': Ma600Out.objects.filter(user=user),  #
            'object_list01': Ma600Out01.objects.filter(user=user),  #

        })
        return context
