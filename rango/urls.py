# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from rango import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^restricted/', views.restricted, name='restricted'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^list/$', views.list, name='list'),
        url(r'^parametres/$', views.parametres, name='parametres'),
        
]