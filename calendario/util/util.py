# -*- coding: utf-8 -*-

def gera_url(id):
	URL = '/calendario/evento/detalhe/'
	return URL + str(id)

def gera_class(classe):
	if classe == 'IMPORTANTE':
		#return 'event-important'
		return '#B40404'
	elif classe == 'ESPECIAL':
		#return 'event-special'
		return '#BE81F7'
	elif classe == 'FERIADO':
		#return 'event-inverse'		
		return '#e6b800'
	elif classe == 'SUCESSO':
		#return 'event-success'
		return '#298A08'
	elif classe == 'INFO':
		#return 'event-info'
		return '#084B8A'
	elif classe == 'ATENÇÃO':
		#return 'event-warning'
		return '#DF7401'
	else:
		return ''

def gera_status(status):
	if status == 'A':
		return 'ATIVO'
	elif status == 'I':
		return 'INATIVO'
	else:
		return ''


