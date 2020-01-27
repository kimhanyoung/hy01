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
from pentions.models import *
from pentions.forms import PostSearchForm
from pentions.views import *

# 홈화면
class PentionView(TemplateView):
    template_name = 'pentions.html'


# 5. 경험생명표별 연금액
class Ma500CreateView(LoginRequiredMixin, CreateView) :
    model = Ma500In
    fields = ['gender','premium','paying_period','present_age','pention_start_age', 'earning_rate','pention_start_rate']
    success_url = reverse_lazy('pentions:ma500result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma500CreateView, self).form_valid(form)

class Ma500ListView(LoginRequiredMixin, ListView):
    template_name = 'pentions/ma500_result.html'
    context_object_name = 'object_list'
    queryset = Ma500Out.objects.all()



