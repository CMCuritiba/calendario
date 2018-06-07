# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .fake.serializers import CalendarioSerializer
from .fake.objects import Calendario
from datetime import datetime

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
