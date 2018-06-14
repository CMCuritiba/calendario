from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model

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