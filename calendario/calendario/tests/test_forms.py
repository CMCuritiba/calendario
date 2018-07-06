# -*- coding: utf-8 -*-

from django.test import TestCase, Client, RequestFactory
from django.db import IntegrityError, DataError
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime

from ..forms import LocalForm, EventoForm, ComunicadoForm
from ..factories import LocalFactory

#--------------------------------------------------------------------------------------
# Teste form Local
#--------------------------------------------------------------------------------------
class LocalFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('zaquinha', password='zaca')
        self.user.is_staff = True
        self.user.lotado = 171
        self.user.matricula = 2179
        self.user.save()
        self.factory = RequestFactory()

    def test_init(self):
        form = LocalForm()

#--------------------------------------------------------------------------------------
# Teste form evento
#--------------------------------------------------------------------------------------
class EventoFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('zaquinha', password='zaca')
        self.user.is_staff = True
        self.user.lotado = 171
        self.user.matricula = 2179
        self.user.save()
        self.factory = RequestFactory()
        self.local = LocalFactory()


    def test_init(self):
        form = EventoForm()

    def test_inclui_ok(self):
        form_data = {'evento':"Palestra de Zacarianismo", 'url':"http://www.cmc.pr.gov.br", 'classe':"ESPECIAL", 'inicio':datetime(2018, 8,30, 9,0), 'fim':datetime(2018, 8,30, 17,0), 'local':1, 'descricao':"Palestra na CMC sobre Zacarianismo",'status':"A"}
        form = EventoForm(form_data)
        #print(form)
        self.assertTrue(form.is_valid()) 

    def test_inclui_evento_local_vazio(self):
        form_data = {'evento': None, 'url':"http://www.cmc.pr.gov.br", 'classe':"ESPECIAL", 'inicio':datetime(2018, 8,30, 9,0), 'fim':datetime(2018, 8,30, 17,0), 'local':1, 'descricao':"Palestra na CMC sobre Zacarianismo",'status':"A"}
        form = EventoForm(form_data)
        self.assertFalse(form.is_valid())

    def test_inclui_inicio_vazio(self):
    	form_data = {'evento': "Palestra de Avezismo", 'url':"http://www.cmc.pr.gov.br", 'classe':"ESPECIAL", 'inicio': None, 'fim':datetime(2018, 8,30, 17,0), 'local':1, 'descricao':"Palestra na CMC sobre Zacarianismo",'status':"A"}
    	form = EventoForm(form_data)
    	self.assertFalse(form.is_valid())

#--------------------------------------------------------------------------------------
# Teste form comunicado
#--------------------------------------------------------------------------------------
class ComunicadoFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('zaquinha', password='zaca')
        self.user.is_staff = True
        self.user.lotado = 171
        self.user.matricula = 2179
        self.user.save()
        self.factory = RequestFactory()

    def test_init(self):
        form = ComunicadoForm()        

    def test_inclui_ok(self):
        form_data = {'titulo':"Titulo comunicado", 'inicio':datetime(2018, 8,30, 9,0), 'fim':datetime(2018, 8,30, 17,0), 'descricao':"Descricao comunicado"}
        form = ComunicadoForm(form_data)
        self.assertTrue(form.is_valid())         

    def test_inclui_titulo_vazio(self):
        form_data = {'titulo': None, 'inicio':datetime(2018, 8,30, 9,0), 'fim':datetime(2018, 8,30, 17,0), 'descricao':"Descricao comunicado"}
        form = ComunicadoForm(form_data)
        self.assertFalse(form.is_valid())                     

    def test_inclui_inicio_vazio(self):
        form_data = {'titulo':"Titulo comunicado", 'inicio': None, 'fim':datetime(2018, 8,30, 17,0), 'descricao':"Descricao comunicado"}
        form = ComunicadoForm(form_data)
        self.assertFalse(form.is_valid())        

    def test_inclui_fim_vazio(self):
        form_data = {'titulo':"Titulo comunicado", 'inicio':datetime(2018, 8,30, 9,0), 'fim': None, 'descricao':"Descricao comunicado"}
        form = ComunicadoForm(form_data)

    def test_inclui_descricao_vazio(self):
        form_data = {'titulo':"Titulo comunicado", 'inicio':datetime(2018, 8,30, 9,0), 'fim':datetime(2018, 8,30, 17,0), 'descricao': None}
        form = ComunicadoForm(form_data)
        self.assertFalse(form.is_valid())                 