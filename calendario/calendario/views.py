# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from calendario.api.fake.serializers import CalendarioSerializer
from calendario.api.fake.objects import Calendario
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, DetailView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator

from autentica.util.mixin import CMCLoginRequired, CMCAdminLoginRequired
from .models import Evento


@method_decorator(xframe_options_sameorigin, name='dispatch')
class CalendarioIndex(SuccessMessageMixin, TemplateView):
	template_name = 'calendario/index.html'

class CalendarioEventoDetails(SuccessMessageMixin, DetailView):
	template_name = 'calendario/evento/details.html'
	model = Evento
