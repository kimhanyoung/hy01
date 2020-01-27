from django.views.generic import ListView
from chartit import DataPool, Chart
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from datetime import datetime
from datetime import date

from mysite.views import LoginRequiredMixin
from funds.models import *
from funds.forms import *
from funds.views import *

# 홈화면
class FundView(TemplateView):
    template_name = 'funds.html'


#--- FormView
class SearchFormView(FormView):
    form_class = FundSearchForm
    template_name = 'Funds/fund_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Ma000fund_list.objects.filter(Q(fund_name__icontains=schWord) | Q(company__icontains=schWord) | Q(fund_type__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class FundUpdateView(LoginRequiredMixin, UpdateView):
    model = Ma000fund_list
    fields = ['fund_name', 'entry_date', 'transfer_date', 'entry_money']
    success_url = reverse_lazy('blog:index')


#fund 검색
class Fa100CreateView(LoginRequiredMixin, CreateView) :
    model = Fa100In
    fields = ['fund_name','company','fund_type','area_section']
    success_url = reverse_lazy('funds:fa100result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Fa100CreateView, self).form_valid(form)

class Fa100ListView(ListView):
    template_name = 'funds/fa100_result.html'
    context_object_name = 'object_list'
    queryset = Fa100Out.objects.all()



