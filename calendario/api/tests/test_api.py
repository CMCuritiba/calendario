from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware
import json

from calendario.calendario.factories import EventoFactory, LocalFactory
from ..views import get_eventos
import datetime

class JSONCalendarioTest(TestCase):
	def setup(self):
		self.factory = APIRequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_url(self):
		response = self.client.get('/api/get_calendario', follow=True)
		self.assertEqual(response.status_code, 200)

	def test_retorna_entradas(self):
		evento = EventoFactory.create()
		response = self.client.get('/api/get_calendario/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertIn('Palestra', data['result'][0]['title'])

	def test_retorna_url(self):
		evento = EventoFactory.create()
		response = self.client.get('/api/get_calendario/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['url'], '/calendario/evento/detalhe/1')

	def test_setor(self):
		evento = EventoFactory.create()
		response = self.client.get('/api/get_calendario/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['setor'], 171)

	def test_pessoa (self):
		evento = EventoFactory.create()
		response = self.client.get('/api/get_calendario/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['pessoa'], 6543)

	def test_cclass (self):
		evento = EventoFactory.create()
		response = self.client.get('/api/get_calendario/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual('event-important', data['result'][0]['class'])

class JSONLocalTest(TestCase):
	def setup(self):
		self.factory = APIRequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_url(self):
		response = self.client.get('/api/get_locais/', follow=True)
		self.assertEqual(response.status_code, 200)

	def test_retorna_entradas(self):
		local = LocalFactory.create()
		response = self.client.get('/api/get_locais/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertIn('Camara', data[0]['local'])

	def test_local(self):
		local = LocalFactory.create()
		response = self.client.get('/api/get_locais/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual('Camara Municipal de Curitiba', data[0]['local'])

	def test_status(self):
		local = LocalFactory.create()
		response = self.client.get('/api/get_locais/', follow=True, pk=1)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual('ATIVO', data[0]['status'])		

class JSONCallSecureLocalExcluiTest(TestCase):
	def setup(self):
		self.factory = APIRequestFactory()
		super(JSONCallSecureLocalExcluiTest, self).setUp()

	def test_dummy(self):
		self.assertEqual(1,1)		

	def test_url(self):
		local = LocalFactory.create()	
		response = self.client.post(
			'/api/local/exclui/', 
			{'pk': 1}
		)

		self.assertEqual(response.status_code, 200)

class JSONEventoTest(TestCase):

	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()
		evento = EventoFactory.create()
	
	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session['setor_id'] = 171
		request.session['pessoa_pessoa'] = 6543
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()		

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_url(self):
		request = self.factory.get('/api/get_eventos/')
		self.setup_request(request)
		response = get_eventos(request)
		self.assertEqual(response.status_code, 200)						

	def test_retorna_entradas(self):
		request = self.factory.get('/api/get_eventos/')
		self.setup_request(request)
		response = get_eventos(request)
		data = json.loads(response.content.decode('utf-8'))
		self.assertIn('Palestra', data[0]['evento'])

	def test_evento(self):
		request = self.factory.get('/api/get_eventos/')
		self.setup_request(request)
		response = get_eventos(request)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual('Palestra Sobre Ponto Biométrico', data[0]['evento'])

	def test_status(self):
		request = self.factory.get('/api/get_eventos/')
		self.setup_request(request)
		response = get_eventos(request)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual('ATIVO', data[0]['status'])				

class JSONCallSecureEventoExcluiTest(TestCase):
	def setup(self):
		self.factory = APIRequestFactory()
		super(JSONCallSecureEventoExcluiTest, self).setUp()

	def test_dummy(self):
		self.assertEqual(1,1)		

	def test_url(self):
		evento = EventoFactory.create()	
		response = self.client.post(
			'/api/evento/exclui/', 
			{'pk': 1}
		)

		self.assertEqual(response.status_code, 200)