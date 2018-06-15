# -*- coding: utf-8 -*-

def gera_url(id):
	URL = '/calendario/evento/detalhe/'
	return URL + str(id)

def gera_class(classe):
	if classe == 'IMPORTANTE':
		return 'event-important'
	elif classe == 'ESPECIAL':
		return 'event-special'
	elif classe == 'INVERSO':
		return 'event-inverse'		
	elif classe == 'SUCESSO':
		return 'event-success'
	elif classe == 'INFO':
		return 'event-info'
	elif classe == 'ATENÇÃO':
		return 'event-warning'
	else:
		return ''

def gera_status(status):
	if status == 'A':
		return 'ATIVO'
	elif status == 'I':
		return 'INATIVO'
	else:
		return ''


