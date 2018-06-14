# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .fake.serializers import CalendarioSerializer
from .fake.objects import Calendario
from datetime import datetime
from django.http import JsonResponse

'''
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

def get_fake_calendario(request):
	entradas = {
		Calendario(id=1, start=datetime(2018, 6, 8, 9, 0), end=datetime(2018, 6, 8, 12, 0), url='http://google.com',  title='Reunião sobre Zacarianismo', setor=4, pessoa=3, cclass='event-inverse'),
		Calendario(id=2, start=datetime(2018, 6, 9, 9, 0), end=datetime(2018, 6, 9, 12, 0), url='http://google.com', title='Reunião sobre Maiquelismo', setor=4, pessoa=3, cclass='event-info'),
		Calendario(id=3, start=datetime(2018, 6, 10, 9, 0), end=datetime(2018, 6, 10, 12, 0), url='http://google.com', title='Reunião sobre Avezismo', setor=4, pessoa=3, cclass='event-warning'),
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
