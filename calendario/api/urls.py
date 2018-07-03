# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'get_fake_calendario', views.FakeCalendarioViewSet, base_name='get_fake_calendario')

urlpatterns = [
	path('get_fake_calendario/', views.get_fake_calendario, name='get_fake_calendario'),
	path('get_calendario/', views.get_calendario, name='get_calendario'),
	path('get_locais/', views.get_locais, name='get_locais'),
	path('get_eventos/', views.get_eventos, name='get_eventos'),
	path('local/exclui/', views.call_local_exclui, name='call-local-exclui'),
	path('evento/exclui/', views.call_evento_exclui, name='call-evento-exclui'),
	path('get_calendario_full/', views.get_calendario_full, name='get_calendario_full'),
]	

#urlpatterns += router.urls
