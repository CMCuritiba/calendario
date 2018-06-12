from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..models import Entry

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

	def test_id(self):
		entry = Entry(ident=1)
		self.assertEqual(1, entry.ident)

	def test_local(self):
		entry = Entry(local="Camara Municipal de Curitiba")
		self.assertEqual(str(entry), entry.local)

	def test_status(self):
		entry = Entry(status="")
		self.assertRaises(TypeError, entry.status)