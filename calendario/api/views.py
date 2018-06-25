# -*- coding: utf-8 -*-

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from datetime import datetime
from django.http import JsonResponse
from calendario.util.util import gera_url, gera_class, gera_status

import json
import datetime

from calendario.calendario.models import Evento, Local
from calendario.calendario.forms import JSONLocalForm, JSONEventoForm

# -----------------------------------------------------------------------------------
# retorna eventos para popular calendário
# -----------------------------------------------------------------------------------
def get_calendario(request):
	entradas = Evento.objects.filter(status='A')

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

# -----------------------------------------------------------------------------------
# chamada API segura para exclusão (inativação de locais)
# -----------------------------------------------------------------------------------
def call_local_exclui(request):
	response = JsonResponse({'status':'false','message':'Erro ao tentar alterar local'}, status=404)

	if request.method == 'POST':
		widget_json = {}
		pk = request.POST.get('pk', None)
		if (pk != None):
			local = Local.objects.get(pk=pk)
			form = JSONLocalForm(request.POST)
			if (form.is_valid()):
				local.status = 'I'
				local.save()
				response = JsonResponse({'status':'true','message':'Local alterado com sucesso'}, status=200)
	return response
# -----------------------------------------------------------------------------------
# retorna lista de eventos
# -----------------------------------------------------------------------------------
def get_eventos(request):
	response = JsonResponse({'status':'false','message':'Você precisa estar logado '}, status=404)

	if request.user.is_anonymous or not request.user.is_authenticated or 'setor_id' not in request.session:
		return response
	else :
		pessoa = request.session['pessoa_pessoa']
		setor = request.session['setor_id']

		entradas = Evento.objects.filter(setor=setor)

		entradas_json = []
		for c in entradas:
			e_json = {}
			e_json['id'] = c.id
			e_json['inicio'] = c.inicio.strftime('%d/%m/%Y')
			e_json['fim'] = c.fim.strftime('%d/%m/%Y')
			e_json['url'] = gera_url(c.id)
			e_json['evento'] = c.evento
			e_json['setor'] = c.setor
			e_json['pessoa'] = c.pessoa
			e_json['status'] = gera_status(c.status)
			e_json['classe'] = gera_class(c.classe)
			entradas_json.append(e_json)

		return JsonResponse(entradas_json, safe=False)		

# -----------------------------------------------------------------------------------
# chamada API segura para exclusão (inativação de eventos)
# -----------------------------------------------------------------------------------
def call_evento_exclui(request):
	response = JsonResponse({'status':'false','message':'Erro ao tentar alterar evento'}, status=404)

	if request.method == 'POST':
		widget_json = {}
		pk = request.POST.get('pk', None)
		if (pk != None):
			evento = Evento.objects.get(pk=pk)
			form = JSONEventoForm(request.POST)
			if (form.is_valid()):
				evento.status = 'I'
				evento.save()
				response = JsonResponse({'status':'true','message':'Evento alterado com sucesso'}, status=200)
	return response		