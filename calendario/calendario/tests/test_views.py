from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from autentica.models import User

from ..views import CalendarioIndex, CalendarioEventoDetails, LocalIndex, LocalCreate, LocalUpdate
from ..factories import EventoFactory, LocalFactory

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

class LocalIndexTest(TestCase):
	
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.save()
		self.factory = RequestFactory()
		evento = EventoFactory.create()

	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()

	def test_dummy(self):
		self.assertEqual(1,1)		

	def test_view_ok(self):
		request = self.factory.get('/calendario/local/index/')
		self.setup_request(request)
		response = LocalIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)				

class LocalCreateTest(TestCase):

	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()		

	def test_dummy(self):
		self.assertEqual(1,1)				

	def test_view_ok(self):
		request = self.factory.get('/calendario/local/novo/')
		self.setup_request(request)
		response = LocalCreate.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						


class LocalUpdateTest(TestCase):
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()

	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()		

	def test_dummy(self):
		self.assertEqual(1,1)				

	def test_view_ok(self):
		request = self.factory.get('/calendario/local/altera/')
		self.setup_request(request)
		request.user = self.user
		local = LocalFactory.create()
		response = LocalUpdate.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/local/update.html')