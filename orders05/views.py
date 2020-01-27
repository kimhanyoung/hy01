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
from orders05.models import *
from orders05.views import *



class Orders05CreateView(LoginRequiredMixin, CreateView) :
    model = Aa01Input
    fields = ['birth_date','end_date']
    #fields = '__all__'
    success_url = reverse_lazy('orders05:result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Orders05CreateView, self).form_valid(form)

class InsuageListView(ListView):
    template_name = 'orders05/aa02result.html'
    context_object_name = 'object_list'
    queryset = Aa02Insuage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(InsuageListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Aa02Insuage.objects.filter(user=user),

        })
        return context
