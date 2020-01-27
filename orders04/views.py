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
from orders04.models import *
from orders04.views import *



class Orders04CreateView(LoginRequiredMixin, CreateView) :
    model = Aa00Input
    fields = ['start_date','end_date']
    #fields = '__all__'
    success_url = reverse_lazy('orders04:result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Orders04CreateView, self).form_valid(form)

class PathmonthListView(ListView):
    template_name = 'orders04/aa01result.html'
    context_object_name = 'object_list'
    queryset = Aa01Pathmonth.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PathmonthListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list00': Aa01Pathmonth.objects.filter(user=user),

        })
        return context


