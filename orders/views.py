from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderItem
from django.db.models import Q
from django.views.generic import ListView
from .forms import OrderCreateForm, FundForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from orders.models import *
from django.urls import reverse_lazy
from mysite.views import LoginRequiredMixin
from django.db.models import Sum
from django.contrib.auth.decorators import permission_required


@permission_required('orders.add_order', login_url='accounts02:list')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.owner = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form': form})


class BasicListView(LoginRequiredMixin,ListView):
    template_name = 'orders/order/orders01_basic.html'
    context_object_name = 'object_list'
    queryset = Aa33Kospirate.objects.all()  # 코스피 과거수익률

    def get_context_data(self, **kwargs):
        context = super(BasicListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Aa33Kospirate.objects.filter(user=user),  # 거치식수익률
            'object_list02': Aa37Kospiaccumrate.objects.filter(user=user),  # 적립식수익률
            #'object_list20': Aa02Fundout.objects.filter(user=user).order_by('fund_no'),         # 펀드 보유현황 출력
            'object_list30': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
            'object_list31': Aa20Kospigraph.objects.filter(user=user).order_by('date'),  # 코스피 그래프
            #'object_list32': Aa30Fundrateout.objects.filter(user=user).order_by('fund'),  # 펀드과거수익률
            'object_list33': Aa27Warning.objects.filter(user=user),  # 펀입비율, 출범일 경고
        })
        return context

# 펀드현황화면
class EearningListView(LoginRequiredMixin, ListView):
    template_name = 'orders/order/orders01_earningrate.html'
    context_object_name = 'object_list'
    queryset = Ab08Averageout.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EearningListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list02': Aa02Fundout.objects.filter(user=user).order_by('fund_no'),  # 펀드 보유현황 출력
            'object_list30': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
            'object_list23': Aa61Totalfundaverage.objects.all(),  # 전체펀드 평균
            'object_list32': Aa30Fundrateout.objects.filter(user=user).order_by('fund'),  # 펀드과거수익률
        })
        return context

#펀드상세화면 입력용
def fund_new(request, result_id):
    item = get_object_or_404(Aa02Fundout, id=result_id)
    initial = {'fund_name': item.fund_name,}

    if request.method == 'POST':
        form = FundForm(request.POST, initial=initial)
        if form.is_valid():
            order = form.save(commit=False)
            order.owner = request.user
            order.item = item
            order.save()
            return redirect('orders:fund_detail')
    else:
        form = FundForm(initial=initial)
    return render(request, 'orders/order/orders01_basicfundform.html', {
        'form': form,
    })

# 펀드상세화면 출력용
class FunddetailView(LoginRequiredMixin, ListView):
    template_name = 'orders/order/orders01_basicfundresult.html'
    context_object_name = 'object_list'
    queryset = Aa47Graphout.objects.all().order_by('basic_date')           # 그래프중 종합주가,가입일

    def get_context_data(self, **kwargs):
        context = super(FunddetailView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list00': Aa47Fundgraphout.objects.all().order_by('basic_date'),  # 그래프중 펀드부분
            'object_list01': Aa48Assetout.objects.all(),         # or with some filter appli
            'object_list02': Aa49Fundout.objects.all(),    # or with some filter appli
            'object_list04': Aa73Fundrate.objects.all(),  # 펀드가입현재 수익률
            'object_list05': Aa76Kospirate.objects.all(),  # 코스피 가입현재 수익률
            'object_list10': Aa53Accumulrate.objects.all(),  # 적립식수익률
            'object_list30': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
        })
        return context

# 해지환급금 화면보여주기
class ReturnmoneyListView(LoginRequiredMixin, ListView):
    template_name = 'orders/order/orders02_returnmoney.html'
    context_object_name = 'object_list'
    queryset = Aa47Graphout.objects.all()    #그냥 넣은것임

    def get_context_data(self, **kwargs):
        context = super(ReturnmoneyListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list01': Ac02Returnmoneyout.objects.filter(user=user).filter(Q(path_month='3')|Q(path_month='6')|Q(path_month='9')|Q(path_month='12')|Q(path_month='24')|Q(path_month='36')|Q(path_month='48')|Q(path_month='60')|Q(path_month='72')|Q(path_month='84')|Q(path_month='96')|Q(path_month='108')|Q(path_month='120')|Q(path_month='180')|Q(path_month='240')|Q(path_month='300')|Q(path_month='360')|Q(path_month='420')|Q(path_month='480')),
            'object_list02': Ac02Returnmoneyout.objects.filter(user=user),   #전체해지환급금
            'object_list20': Ab06Presentpayment.objects.filter(user=user),  #
            #'object_list25': Ab07Listout.objects.all(),  # 생보해지환급금 회사별 리스트출력
            'object_list26': Ab08Averageout.objects.all(),  # 생보해지환급금 전체평균
            'object_list30': Aa02Enterout.objects.filter(user=user),  # 보험가입내역 출력
        })
        return context

# 예상연금액보여주기
class PentionListView(LoginRequiredMixin, ListView):
    template_name = 'orders/order/orders03_pention.html'
    context_object_name = 'object_list'
    queryset = Aa47Graphout.objects.all()    #그냥 넣은것임

    def get_context_data(self, **kwargs):
        context = super(PentionListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list00': Ac04Pentionout.objects.filter(user=user),
            'object_list01': Ac03Pentionmoney.objects.filter(user=user),       # or with some filter appli
            'object_list02': Ac02Returnmoneyout.objects.filter(user=user),  # or with some filter appli
        })
        return context

#1. 적립식펀드
class FundCreateView(LoginRequiredMixin, CreateView) :
    model = Fund03In
    template_name = 'orders/order/orders_fund01in.html'
    fields = ['entry_date','premium','fund_type']

    success_url = reverse_lazy('orders:fundresult')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FundCreateView, self).form_valid(form)


class FundListView(LoginRequiredMixin, ListView):
    template_name = 'orders/order/orders_fund02out.html'
    context_object_name = 'object_list'
    queryset = Fund05List.objects.all()

    def get_context_data(self, **kwargs):
        context = super(FundListView, self).get_context_data(**kwargs)
        user = self.request.user
        context.update({
            'object_list00': Fund05List.objects.filter(user=user),
            'object_list01': Fund06Tex.objects.filter(user=user).order_by('tex_date'),
            'object_list02': Fund09Result.objects.filter(user=user),
            'object_list03': Fund10Entry.objects.filter(user=user),
            'object_list04': Fund06Tex.objects.filter(user=user).aggregate(Sum('tex'))['tex__sum'],           #결산세금의 합계
        })
        return context


