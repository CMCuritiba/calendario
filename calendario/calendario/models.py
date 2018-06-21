# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError

from tinymce import HTMLField

from datetime import datetime

#---------------------------------------------------------------------------------------------
# Model Local
#---------------------------------------------------------------------------------------------

class Local(models.Model):

	STATUS_ATIVO = 'A'
	STATUS_INATIVO = 'I'
	STATUS_CHOICES = (
		(STATUS_ATIVO, 'ATIVO'),
		(STATUS_INATIVO, 'INATIVO')
	)

	local = models.CharField(max_length=300)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_ATIVO)

	def __unicode__(self):
		return self.local

	def __str__(self):
		return self.local		
    
#---------------------------------------------------------------------------------------------
# Model Evento
#---------------------------------------------------------------------------------------------
class Evento(models.Model):
	class Meta:
		verbose_name_plural = 'Eventos'

	CLASSE_IMPORTANTE = 'IMPORTANTE'
	CLASSE_ESPECIAL = 'ESPECIAL'
	CLASSE_INVERSO = 'INVERSO'
	CLASSE_SUCESSO = 'SUCESSO'
	CLASSE_INFO = 'INFO'
	CLASSE_ATENCAO = 'ATENÇÃO'
	CLASSE_NULO = None
	CLASSE_CHOICES = (
		(CLASSE_IMPORTANTE, 'IMPORTANTE'),
		(CLASSE_ESPECIAL, 'ESPECIAL'),
		(CLASSE_INVERSO, 'INVERSO'),
		(CLASSE_SUCESSO, 'SUCESSO'),
		(CLASSE_INFO, 'INFO'),
		(CLASSE_ATENCAO, 'ATENÇÃO'),
		(CLASSE_NULO, 'NULO'),
	)

	STATUS_ATIVO = 'A'
	STATUS_INATIVO = 'I'
	STATUS_CHOICES = (
		(STATUS_ATIVO, 'ATIVO'),
		(STATUS_INATIVO, 'INATIVO')
	)

	evento = models.CharField(max_length=300)
	url = models.CharField(null=True, blank=True, max_length=100)
	classe = models.CharField(max_length=10, null=True, blank=True, choices=CLASSE_CHOICES, default=CLASSE_NULO)
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	local = models.ForeignKey(Local, models.CASCADE)
	descricao = HTMLField(null=True, blank=True)
	pessoa = models.IntegerField()
	setor = models.IntegerField()
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_ATIVO)