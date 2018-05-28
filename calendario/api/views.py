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
		1: Calendario(id=1, data=datetime(2018, 5,28, 9,0), descricao='Reunião sobre Zacarianismo'),
		2: Calendario(id=2, data=datetime(2018, 5,29, 9,0), descricao='Reunião sobre Maiquelismo'),
		3: Calendario(id=3, data=datetime(2018, 5,30, 9,0), descricao='Reunião sobre Avezismo'),
	}			

	def list(self, request):
		serializer = CalendarioSerializer(
			instance = self.entradas.values(), many=True
		)
		return Response(serializer.data)
