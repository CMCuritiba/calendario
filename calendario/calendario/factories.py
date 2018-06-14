# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from datetime import datetime

from .models import Local
from .models import Evento

class LocalFactory(DjangoModelFactory):
	class Meta:
		model = Local
	id = 1
	local = 'Camara Municipal de Curitiba'
	status = 'A'

class EventoFactory(DjangoModelFactory):
	class Meta:
		model = Evento

	id = 1
	evento = 'Palestra Sobre Ponto Biométrico'
	url = 'http://www.cmc.pr.gov.br'
	classe = 'IMPORTANTE'
	inicio = datetime(2018, 6, 8, 12, 0)
	fim = datetime(2018, 6, 8, 18, 0)
	local = 1
	pessoa = 6543
	setor = 171