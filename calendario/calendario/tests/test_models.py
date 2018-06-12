# -*- coding: utf-8 -*-

from django.test import TestCase, Client, RequestFactory
from django.db import IntegrityError, DataError
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime

from ..factories import EventoFactory

class LocalModelTest(TestCase):
	
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.save()
		self.factory = RequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

class EventoModelTest(TestCase):

	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.save()
		self.factory = RequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_evento_insere_ok(self):
		evento = EventoFactory.create()
		self.assertEqual(evento.id, 1)
		self.assertEqual(evento.evento, 'Palestra Sobre Ponto Biométrico')
		self.assertEqual(evento.url, 'http://www.cmc.pr.gov.br')
		self.assertEqual(evento.classe, 'IMPORTANTE')
		self.assertEqual(evento.inicio, datetime(2018, 6, 8, 12, 0))
		self.assertEqual(evento.fim, datetime(2018, 6, 8, 18, 0))
		self.assertEqual(evento.pessoa, 6543)
		self.assertEqual(evento.setor, 171)
		self.assertEqual(evento.local, 1)

	def test_evento_insere_evento_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(evento=None)
	
	def test_evento_insere_url_nulo(self):			
		evento = EventoFactory.create(url=None)
		self.assertEqual(evento.id, 1)

	def test_evento_insere_classe_nulo(self):			
		evento = EventoFactory.create(classe=None)
		self.assertEqual(evento.id, 1)

	def test_evento_insere_inicio_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(inicio=None)

	def test_evento_insere_fim_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(fim=None)

	def test_evento_insere_pessoa_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(pessoa=None)			

	def test_evento_insere_setor_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(setor=None)			

	def test_evento_insere_local_nulo(self):
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create(local=None)

	def test_evento_duplicado_ok(self):
		evento = EventoFactory.create()
		with self.assertRaises(IntegrityError):
			evento = EventoFactory.create()