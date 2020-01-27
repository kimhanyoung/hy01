from django.views.generic import ListView
from django.shortcuts import render_to_response, render
from django.urls import reverse_lazy


from mysite.views import LoginRequiredMixin
from orders06.models import *
from orders06.views import *

# . 흥부와 놀부     -- 둘다 listview
class HungbuListView(ListView) :
    template_name = 'orders06/md300.html'
    context_object_name = 'object_list'
    queryset = HungbuOut.objects.all()


class HungbuListView02(ListView):
    template_name = 'orders06/md300_result.html'
    context_object_name = 'object_list'
    queryset = HungbuOut02.objects.all()

