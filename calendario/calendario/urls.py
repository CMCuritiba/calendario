# -*- coding: utf-8 -*-

from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.CalendarioIndex.as_view(), name='index'),
]	