# -*- coding: utf-8 -*-

from factory.django import DjangoModelFactory
from factory import SubFactory
from datetime import datetime

from .models import Local, Evento, Comunicado

#--------------------------------------------------------------------------------------
# Factory local
#--------------------------------------------------------------------------------------
class LocalFactory(DjangoModelFactory):
	class Meta:
		model = Local
	id = 1
	local = 'Camara Municipal de Curitiba'
	status = 'A'

#--------------------------------------------------------------------------------------
# Factory evento
#--------------------------------------------------------------------------------------
class EventoFactory(DjangoModelFactory):
	class Meta:
		model = Evento
	id = 1
	evento = 'Palestra Sobre Ponto Biométrico'
	url = '/calendario/evento/detalhe/1'
	classe = 'IMPORTANTE'
	inicio = datetime(2018, 6, 8, 12, 0)
	fim = datetime(2018, 6, 8, 18, 0)
	local = SubFactory(LocalFactory)
	pessoa = 6543
	setor = 171

#--------------------------------------------------------------------------------------
# Factory comunicado
#--------------------------------------------------------------------------------------
class ComunicadoFactory(DjangoModelFactory):
	class Meta:
		model = Comunicado
	id = 1
	titulo = 'Aviso comunicado'
	inicio = datetime(2018, 6, 8, 12, 0)
	fim = datetime(2018, 6, 8, 18, 0)
	descricao = 'Aviso de comunicado importante'