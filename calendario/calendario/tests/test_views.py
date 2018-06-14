from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..views import CalendarioIndex, CalendarioEventoDetails
from ..factories import EventoFactory

class CalendarioIndexTest(TestCase):
	
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		#self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		#self.user.is_staff = True
		#self.user.save()
		self.factory = RequestFactory()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_index(self):
		request = self.factory.get('/calendario/')
		response = CalendarioIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)

class CalendarioEventoDetailsTest(TestCase):
	
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		#self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		#self.user.is_staff = True
		#self.user.save()
		self.factory = RequestFactory()
		evento = EventoFactory.create()

	def test_dummy(self):
		self.assertEqual(1,1)

	def test_view_ok(self):
		request = self.factory.get('/calendario/evento/details/')
		response = CalendarioEventoDetails.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)		