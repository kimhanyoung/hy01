from django.urls import re_path, include, path
from django.contrib import admin


from mysite.views import HomeView
from mysite.views import UserCreateView, UserCreateDoneTV


urlpatterns = [

    re_path(r'^$', HomeView.as_view(), name="home"),

    # 로그인 기능 아래 3가지
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
    re_path(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    re_path(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),

    re_path(r'^pentions/', include('pentions.urls')),
    re_path(r'^pentions01/', include('pentions01.urls')),
    re_path(r'^pentionsto/', include('pentionsto.urls')),

    re_path(r'^blog01/', include('blog01.urls')),
    re_path(r'^funds/', include('funds.urls')),
    re_path(r'^vund/', include('vund.urls')),
    re_path(r'^shop/', include('shop.urls')),

    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('orders02/', include('orders02.urls')),
    path('orders03/', include('orders03.urls')),
    path('orders04/', include('orders04.urls')),
    path('orders05/', include('orders05.urls')),
    path('orders06/', include('orders06.urls')),
    path('orders07/', include('orders07.urls')),
    path('accounts02/', include('accounts02.urls')),

    re_path(r'^admin/', admin.site.urls),

]


