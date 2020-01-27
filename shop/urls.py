from django.urls import path, re_path
from shop import views
from shop.views import *

app_name = 'shop'

urlpatterns = [

    re_path(r'^$', SearchFormView.as_view(), name='product_all'),
    re_path(r'^(?P<category_id>\d+)/$', views.detail, name='category_detail'),

    path('<int:id>/<product_slug>/', product_detail, name='product_detail'),
]



#path('', product_in_category, name='product_all'),
#path('<slug:category_slug>/', product_in_category, name='product_in_category'),