# -*- coding: utf-8 -*-

from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.CalendarioIndex.as_view(), name='index'),
	path('evento/detalhe/<int:pk>/', views.CalendarioEventoDetails.as_view(), name='evento-details'),
	path('local/', views.LocalIndex.as_view(), name='local-index'),
]	
