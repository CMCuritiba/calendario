# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers
from . import views

#router = routers.DefaultRouter()
#router.register(r'get_fake_calendario', views.FakeCalendarioViewSet, base_name='get_fake_calendario')

urlpatterns = [
	path('get_calendario/', views.get_calendario, name='get_calendario'),
	path('get_locais/', views.get_locais, name='get_locais'),
	path('local/exclui/', views.call_local_exclui, name='call-local-exclui'),
	path('get_eventos/', views.get_eventos, name='get_eventos'),
	path('evento/exclui/', views.call_evento_exclui, name='call-evento-exclui'),
]	

#urlpatterns += router.urls
