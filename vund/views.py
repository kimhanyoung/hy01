from django.views.generic import ListView
from chartit import DataPool, Chart
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy                                 #장고 2.0에서 경로변경
from django.views.generic.edit import FormView
from datetime import datetime
from datetime import date

from mysite.views import LoginRequiredMixin
from vund.models import *
from vund.forms import *
from vund.views import *

# 홈화면
class VundView(TemplateView):
    template_name = 'vund.html'


#--- FormView
class SearchFormView(FormView):
    form_class = VundSearchForm
    template_name = 'Vund/vund_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Ma000insu_list.objects.filter(Q(insu_name_d_icontains=schWord) | Q(company__icontains=schWord) ).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

class VundUV(LoginRequiredMixin, UpdateView):
    model = Ma000insu_list
    fields = ['insu_name','company']
    # success_url = reverse_lazy('vund:ma100')

    def get_context_data(self, **kwargs):
        context = super(VundUV, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = VundInlineFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = VundInlineFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.object.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


















