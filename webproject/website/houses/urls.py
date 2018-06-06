from django.urls import path, re_path, include
from . import views



urlpatterns= [
    path(r'', views.houses_list, name='Houses'),
    path(r'create/',views.house_create, name='create'),
    re_path(r'^(?P<house_name>[\w-]+)/$', views.house_detail, name='detail'),

]

 