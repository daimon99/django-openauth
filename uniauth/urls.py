# coding: utf-8
from uniauth import views
from django.urls import path

urlpatterns = [
    path('login/', views.UniAuthView.as_view(), name='login'),
]
