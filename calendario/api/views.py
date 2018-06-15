# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .fake.serializers import CalendarioSerializer
from .fake.objects import Calendario
from datetime import datetime
from django.http import JsonResponse
from calendario.util.util import gera_url, gera_class, gera_status

from calendario.calendario.models import Evento, Local

'''
# -----------------------------------------------------------------------------------
# fake calendario usando django_rest
# -----------------------------------------------------------------------------------
class FakeCalendarioViewSet(viewsets.ViewSet):
	serializer_class = CalendarioSerializer

	entradas = {
		1: Calendario(id=1, start=datetime(2018, 5,28, 9,0), end=datetime(2018, 5,30, 15,0), url='teste_url_evento',  title='Reunião sobre Zacarianismo', setor=4, pessoa=3, cclass='event-inverse'),
		2: Calendario(id=2, start=datetime(2018, 5,29, 9,0), end=datetime(2018, 5,30, 15,0), url='teste_url_evento', title='Reunião sobre Maiquelismo', setor=4, pessoa=3, cclass='event-info'),
		3: Calendario(id=3, start=datetime(2018, 5,30, 9,0), end=datetime(2018, 5,30, 15,0), url='teste_url_evento', title='Reunião sobre Avezismo', setor=4, pessoa=3, cclass='event-warning'),
	}			

	def list(self, request):
		serializer = CalendarioSerializer(
			instance = self.entradas.values(), many=True
		)
		return Response(serializer.data)
'''

# -----------------------------------------------------------------------------------
# fake calendario 
# -----------------------------------------------------------------------------------
def get_fake_calendario(request):
	entradas = {
		Calendario(id=1, start=datetime(2018, 6, 8, 9, 0), end=datetime(2018, 6, 8, 12, 0), url='http://google.com',  title='Reunião - Saúde - Audiência Pública', setor=4, pessoa=3, cclass='event-inverse'),
		Calendario(id=2, start=datetime(2018, 6, 9, 9, 0), end=datetime(2018, 6, 9, 12, 0), url='http://google.com', title='6ª Reunião ORDINÁRIA DA COMISSÃO DE SAÚDE, BEM ESTAR SOCIAL E ESPORTE', setor=4, pessoa=3, cclass='event-info'),
		Calendario(id=3, start=datetime(2018, 6, 9, 9, 0), end=datetime(2018, 6, 9, 12, 0), url='http://google.com', title='Reunião - Educação', setor=4, pessoa=3, cclass='event-info'),
		Calendario(id=4, start=datetime(2018, 6, 10, 9, 0), end=datetime(2018, 6, 10, 12, 0), url='http://google.com', title='Reunião - Audiência Pública LDO2019', setor=4, pessoa=3, cclass='event-warning'),
	}

	entradas_json = []
	for c in entradas:
		e_json = {}
		e_json['id'] = c.id
		e_json['start'] = int(c.start.timestamp() * 1000)
		e_json['end'] = int(c.end.timestamp() * 1000)
		e_json['url'] = c.url
		e_json['title'] = c.title
		e_json['setor'] = c.setor
		e_json['pessoa'] = c.pessoa
		e_json['class'] = c.cclass
		entradas_json.append(e_json)

	responseData = {
		"success": 1,
		"result": entradas_json
	}

	return JsonResponse(responseData, safe=True)

# -----------------------------------------------------------------------------------
# retorna eventos para popular calendário
# -----------------------------------------------------------------------------------
def get_calendario(request):
	entradas = Evento.objects.all()

	entradas_json = []
	for c in entradas:
		e_json = {}
		e_json['id'] = c.id
		e_json['start'] = int(c.inicio.timestamp() * 1000)
		e_json['end'] = int(c.fim.timestamp() * 1000)
		e_json['url'] = gera_url(c.id)
		e_json['title'] = c.evento
		e_json['setor'] = c.setor
		e_json['pessoa'] = c.pessoa
		e_json['class'] = gera_class(c.classe)
		entradas_json.append(e_json)

	responseData = {
		"success": 1,
		"result": entradas_json
	}

	return JsonResponse(responseData, safe=True)	

# -----------------------------------------------------------------------------------
# retorna lista de locais
# -----------------------------------------------------------------------------------
def get_locais(request):
	entradas = Local.objects.all().order_by("local")

	entradas_json = []
	for c in entradas:
		e_json = {}
		e_json['id'] = c.id
		e_json['local'] = c.local
		e_json['status'] = gera_status(c.status)
		entradas_json.append(e_json)

	return JsonResponse(entradas_json, safe=False)		
