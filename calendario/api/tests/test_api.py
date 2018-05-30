from rest_framework.test import APITestCase, APIRequestFactory, APIClient
from django.test import TestCase, Client
from django.urls import reverse


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
		self.assertEqual(response.data[0]['descricao'], 'Reunião sobre Zacarianismo')

	def test_setor(self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		self.assertEqual(response.data[0]['setor'], 4)

	def test_pessoa (self):
		response = self.client.get('/api/get_fake_calendario', follow=True)
		self.assertEqual(response.data[1]['pessoa'], 3)