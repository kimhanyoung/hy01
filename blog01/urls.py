from django.urls import re_path
from blog01.views import *
from blog01 import views

app_name = 'blog01'
urlpatterns = [

    # Example: /
    re_path(r'^$', PostLV.as_view(), name='index'),

    # Example: /post/ (same as /)
    re_path(r'^post/$', PostLV.as_view(), name='post_list'),

    # Example: /post/django-example/
    re_path(r'^post/(?P<pk>[-\w]+)/$', PostDV.as_view(), name='post_detail'),

    # Example: /add/
    re_path(r'^add/$',
        PostCreateView.as_view(), name="add",
    ),

    #re_path(r'^add/$', views.upload_file, name='add'),


    # Example: /change/
    re_path(r'^change/$',
        PostChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    re_path(r'^(?P<pk>[0-9]+)/update/$',
        PostUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    re_path(r'^(?P<pk>[0-9]+)/delete/$',
        PostDeleteView.as_view(), name="delete",
    ),
]