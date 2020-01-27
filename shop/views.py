from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
from mysite.views import LoginRequiredMixin

from shop.forms import CategorySearchForm
from .models import *


#--- FormView
class SearchFormView(FormView):
    form_class = CategorySearchForm
    template_name = 'shop/list.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        category_list = Category.objects.filter(Q(insu_name__icontains=schWord) | Q(company__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['categories'] = category_list

        return render(self.request, self.template_name, context)

@login_required
def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category_id = category_id)
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})



from cart.forms import AddProductForm
def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':100})
    return render(request, 'shop/detail.html', {'product': product, 'add_to_cart':add_to_cart})
