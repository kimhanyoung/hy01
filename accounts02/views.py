from django.views.generic import ListView
from chartit import DataPool, Chart
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from mysite.views import LoginRequiredMixin
from orders07.models import *
from accounts02.views import *


class AccountsListview(LoginRequiredMixin, ListView):
    template_name = 'accounts02/account_list.html'

    def get_queryset(self):
        return Metfund.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AccountsListview, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Aa01Totalcount.objects.all(),  #

        })
        return context