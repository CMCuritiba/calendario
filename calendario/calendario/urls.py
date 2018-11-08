# -*- coding: utf-8 -*-

from django.urls import include, path
from . import views

urlpatterns = [
	path('evento/detalhe/<int:pk>/', views.CalendarioEventoDetails.as_view(), name='evento-details'),
	path('local/', views.LocalIndex.as_view(), name='local-index'),
	path('local/novo/', views.LocalCreate.as_view(), name='local-novo'),
	path('local/altera/<int:pk>/', views.LocalUpdate.as_view(), name='local-altera'),
	path('evento/', views.EventoIndex.as_view(), name='evento-index'),
	path('evento/novo/', views.EventoCreate.as_view(), name='evento-novo'),
	path('evento/altera/<int:pk>/', views.EventoUpdate.as_view(), name='evento-altera'),
	path('comunicado/', views.ComunicadoIndex.as_view(), name='comunicado-index'),
	path('comunicado/novo/', views.ComunicadoCreate.as_view(), name='comunicado-novo'),
	path('comunicado/altera/<int:pk>/', views.ComunicadoUpdate.as_view(), name='comunicado-altera'),
	path('', views.FullCalendarioBotaoIndex.as_view(), name='index'),
]	
