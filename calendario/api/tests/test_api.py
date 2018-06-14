from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.test import TestCase, Client
from django.urls import reverse
import json


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