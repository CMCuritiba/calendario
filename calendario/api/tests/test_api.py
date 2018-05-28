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
		print(response.data)
		self.assertEqual(response.data[0]['descricao'], 'Reunião sobre Zacarianismo')				