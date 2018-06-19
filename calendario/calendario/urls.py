# -*- coding: utf-8 -*-

from django.urls import include, path
from . import views

urlpatterns = [
	path('', views.CalendarioIndex.as_view(), name='index'),
	path('evento/detalhe/<int:pk>/', views.CalendarioEventoDetails.as_view(), name='evento-details'),
	path('local/', views.LocalIndex.as_view(), name='local-index'),
	path('local/novo/', views.LocalCreate.as_view(), name='local-novo'),
	path('local/altera/<int:pk>/', views.LocalUpdate.as_view(), name='local-altera'),
]	
