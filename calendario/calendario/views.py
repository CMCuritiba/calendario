# -*- coding: utf-8 -*-

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from datetime import datetime
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, DetailView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse

from autentica.util.mixin import CMCLoginRequired, CMCAdminLoginRequired
from .models import Evento, Local
from .forms import LocalForm, EventoForm


#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class CalendarioIndex(SuccessMessageMixin, TemplateView):
	template_name = 'calendario/index.html'

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class CalendarioEventoDetails(SuccessMessageMixin, DetailView):
	template_name = 'calendario/evento/details.html'
	model = Evento

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class LocalIndex(CMCLoginRequired, SuccessMessageMixin, TemplateView):
    template_name = 'calendario/local/index.html'	

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------    
class EventoIndex(CMCLoginRequired, SuccessMessageMixin, TemplateView):
    template_name = 'calendario/evento/index.html'

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class LocalCreate(CMCAdminLoginRequired, SuccessMessageMixin, CreateView):
    model = Local
    form_class = LocalForm
    success_url = '/calendario/local/'
    success_message = "Local criado com sucesso"
    template_name = 'calendario/local/create.html'   

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class LocalUpdate(CMCAdminLoginRequired, SuccessMessageMixin, UpdateView):
    model = Local
    form_class = LocalForm
    success_url = '/calendario/local/'
    success_message = "Local alterado com sucesso"
    template_name = 'calendario/local/update.html'       

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class EventoCreate(CMCAdminLoginRequired, SuccessMessageMixin, CreateView):
    model = Evento
    form_class = EventoForm
    success_url = '/calendario/evento/'
    success_message = "Evento criado com sucesso"
    template_name = 'calendario/evento/create.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.setor = self.request.session['setor_id']
        obj.pessoa = self.request.session['pessoa_pessoa']
        obj.save()
        return super(EventoCreate, self).form_valid(form)

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class EventoUpdate(CMCAdminLoginRequired, SuccessMessageMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    success_url = '/calendario/evento/'
    success_message = "Evento alterado com sucesso"
    template_name = 'calendario/evento/update.html'           

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.setor = self.request.session['setor_id']
        obj.pessoa = self.request.session['pessoa_pessoa']
        obj.save()
        return super(EventoUpdate, self).form_valid(form)

#--------------------------------------------------------------------------------------
#
#--------------------------------------------------------------------------------------
class FullCalendarioIndex(SuccessMessageMixin, TemplateView):
    template_name = 'calendario/index_full.html'        

#--------------------------------------------------------------------------------------
# Classe index comunicado
#--------------------------------------------------------------------------------------    
class ComunicadoIndex(CMCLoginRequired, SuccessMessageMixin, TemplateView):
    template_name = 'calendario/comunicado/index.html'    