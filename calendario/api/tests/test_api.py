from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.test import TestCase, Client
from django.urls import reverse
import json

from calendario.calendario.factories import EventoFactory


class JSONFakeTest(TestCase):
	def setup(self):
		self.factory = APIRequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_url(self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		self.assertEqual(response.status_code, 200)

	def test_retorna_entradas(self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		data = json.loads(response.content.decode('utf-8'))
		self.assertIn('Reunião', data['result'][0]['title'])

	def test_retorna_url(self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['url'], 'http://google.com')

	def test_setor(self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['setor'], 4)

	def test_pessoa (self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		data = json.loads(response.content.decode('utf-8'))
		self.assertEqual(data['result'][0]['pessoa'], 3)

	def test_cclass (self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		data = json.loads(response.content.decode('utf-8'))
		self.assertIn('event', data['result'][0]['class'])


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
