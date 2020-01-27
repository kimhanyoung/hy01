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

#1. 투자의 원칙(1) 시간의 가치
class Ma100CreateView(LoginRequiredMixin, CreateView) :
    model = Ma100In
    fields = ['premium','paying_period','earning_rate', 'chulsu_start_year','result_year']
    #fields = '__all__'
    success_url = reverse_lazy('pentions:ma100result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma100CreateView, self).form_valid(form)

class Ma100ListView(ListView):
    template_name = 'pentions/ma100_result.html'
    context_object_name = 'object_list'
    queryset = Ma100Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Ma100ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ma100Out.objects.filter(user=user).filter(Q(year='1')|Q(year='2')|Q(year='3')|Q(year='4')|Q(year='5')|Q(year='6')|Q(year='7')|Q(year='8')|Q(year='9')|Q(year='10')|Q(year='15')|Q(year='20')|Q(year='25')|Q(year='30')|Q(year='35')|Q(year='40')),  #
            'object_list02': Ma100Out02.objects.filter(user=user),
            'object_list03': Ma100Out.objects.filter(user=user).order_by('year')

        })
        return context

# 2. 투자의 원칙(2) 수익률
class Ma200CreateView(LoginRequiredMixin, CreateView) :
    model = Ma200In
    fields = ['premium','paying_period','younghee_earning_rate','chulsu_earning_rate', 'result_year']
    success_url = reverse_lazy('pentions:ma200result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma200CreateView, self).form_valid(form)

class Ma200ListView(LoginRequiredMixin, ListView):
    template_name = 'pentions/ma200_result.html'
    context_object_name = 'object_list'
    queryset = Ma200Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Ma200ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ma200Out.objects.filter(user=user).filter(Q(year='1')|Q(year='2')|Q(year='3')|Q(year='4')|Q(year='5')|Q(year='6')|Q(year='7')|Q(year='8')|Q(year='9')|Q(year='10')|Q(year='15')|Q(year='20')|Q(year='25')|Q(year='30')|Q(year='35')|Q(year='40')),  #
            'object_list02': Ma200Out.objects.filter(user=user),
            'object_list03': Ma200Out02.objects.filter(user=user)

        })
        return context


# 3. 투자의 원칙(3) 세금
class Ma300CreateView(LoginRequiredMixin, CreateView) :
    model = Ma300In
    fields = ['premium','paying_period','younghee_earning_rate','chulsu_earning_rate', 'result_year']
    success_url = reverse_lazy('pentions:ma300result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma300CreateView, self).form_valid(form)

class Ma300ListView(LoginRequiredMixin, ListView):
    template_name = 'pentions/ma300_result.html'
    context_object_name = 'object_list'
    queryset = Ma300Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Ma300ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ma300Out.objects.filter(user=user).filter(Q(year='1')|Q(year='2')|Q(year='3')|Q(year='5')|Q(year='10')|Q(year='15')|Q(year='20')|Q(year='25')|Q(year='30')|Q(year='35')|Q(year='40')),  #
            'object_list02': Ma300Out.objects.filter(user=user)

        })
        return context



# 4. 연금액계산 (qusdor)
class Ma400CreateView(LoginRequiredMixin, CreateView) :
    model = Ma400In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'earning_rate','pention_start_rate']
    success_url = reverse_lazy('pentions:ma400result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Ma400CreateView, self).form_valid(form)


class Ma400ListView(LoginRequiredMixin, ListView):
    template_name = 'pentions/ma400_result.html'
    context_object_name = 'object_list'
    queryset = Ma400Out.objects.all()

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





# 6. 연금예상액(일시금)
class Mc100CreateView(LoginRequiredMixin, CreateView) :
    model = Mc100In
    fields = ['gender','pention_start_rate','reserve_money', 'present_age','life_expectancy']
    success_url = reverse_lazy('pentions:mc100result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Mc100CreateView, self).form_valid(form)

class Mc100ListView(LoginRequiredMixin, ListView):
    model = Mc100Out
    template_name = 'pentions/mc100_result.html'

    def get_context_data(self, **kwargs):
        context = super(Mc100ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Mc100Out.objects.filter(user=user)

        })
        return context

# 7. 월목표연금액
class Mc200CreateView(LoginRequiredMixin, CreateView) :
    model = Mc200In
    fields = ['target_pention','gender','paying_period','present_age','pention_start_age', 'earning_rate','public_rate','pention_start_rate']
    success_url = reverse_lazy('pentions:mc200result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Mc200CreateView, self).form_valid(form)


class Mc200ListView(ListView):
    template_name = 'pentions/mc200_result.html'
    context_object_name = 'object_list'
    queryset = Mc200Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Mc200ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Mc200Out.objects.filter(user=user)

        })
        return context


# 8. 연금개시후 공시이율
class Mc300CreateView(LoginRequiredMixin, CreateView) :
    model = Mc300In
    fields = ['gender','premium','paying_period','present_age','pention_start_age', 'earning_rate','first_pention_start_rate','second_pention_start_rate']
    success_url = reverse_lazy('pentions:mc300result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Mc300CreateView, self).form_valid(form)

class Mc300ListView(ListView):
    template_name = 'pentions/mc300_result.html'
    context_object_name = 'object_list'
    queryset = Mc300Out01.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Mc300ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Mc300Out01.objects.filter(user=user),
            'object_list02': Mc300Out02.objects.filter(user=user)

        })
        return context


# 9. 변액연금비용
class Md100CreateView(LoginRequiredMixin, CreateView) :
    model = Md100In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'earning_rate']
    success_url = reverse_lazy('pentions:md100result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Md100CreateView, self).form_valid(form)

class Md100ListView(ListView):
    template_name = 'pentions/md100_result.html'
    context_object_name = 'object_list'
    queryset = Md100Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Md100ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Md100Out.objects.filter(user=user),
            'object_list02': Md100Out01.objects.filter(user=user)

        })
        return context




# . 위험보험료
class Md200CreateView(LoginRequiredMixin, CreateView) :
    model = Md200In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'risk_premium']
    success_url = reverse_lazy('pentions:md200result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Md200CreateView, self).form_valid(form)

class Md200ListView(ListView):
    template_name = 'pentions/md200_result.html'
    context_object_name = 'object_list'
    queryset = Md200Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Md200ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Md200Out.objects.filter(user=user)

        })
        return context




# . 적금의 비밀
class Mg100CreateView(LoginRequiredMixin, CreateView) :
    model = Mg100In
    fields = ['deposit_rate','premium']
    success_url = reverse_lazy('pentions:mg100result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Mg100CreateView, self).form_valid(form)

class Mg100ListView(ListView):
    template_name = 'pentions/mg100_result.html'
    context_object_name = 'object_list'
    queryset = Mg100Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Mg100ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Mg100Out.objects.filter(user=user)

        })
        return context


# . 수익률별 연금예상액
class Mh200CreateView(LoginRequiredMixin, CreateView):
    model = Mh200In
    fields = ['gender','start_year','start_month','premium','paying_period','present_age','pention_start_age', 'a_earning_rate','b_earning_rate','pention_start_rate']
    success_url = reverse_lazy('pentions:mh200result')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(Mh200CreateView, self).form_valid(form)

class Mh200ListView(ListView):
    template_name = 'pentions/mh200_result.html'
    context_object_name = 'object_list'
    queryset = Mh200Out.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Mh200ListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Mh200Out.objects.filter(user=user)

        })
        return context