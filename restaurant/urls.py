from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from restaurant.views import index, detail

app_name = 'restaurant'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Restaurant_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^CustomerRegister/$', views.CustomerRegister, name='CustomerRegister'),
    ]