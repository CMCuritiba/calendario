from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from autentica.models import User

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60
from ..views import CalendarioIndex, CalendarioEventoDetails, LocalIndex, LocalCreate, LocalUpdate, EventoIndex, EventoUpdate
from ..factories import EventoFactory, LocalFactory
=======
from ..views import CalendarioIndex, CalendarioEventoDetails, LocalIndex, EventoIndex
from ..factories import EventoFactory
>>>>>>> issue31

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
		self.assertEqual(response.template_name[0], 'calendario/evento/index.html')

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
<<<<<<< HEAD
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/local/update.html')
<<<<<<< HEAD
=======
		self.assertEqual(response.status_code, 200)						

class EventoUpdateTest(TestCase):
=======

class EventoIndexTest(TestCase):
	
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
<<<<<<< HEAD
		self.user.is_superuser = True
		self.user.save()
		self.factory = RequestFactory()
=======
		self.user.save()
		self.factory = RequestFactory()
		evento = EventoFactory.create()
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60

	def setup_request(self, request):
		request.user = self.user

		middleware = SessionMiddleware()
		middleware.process_request(request)
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
<<<<<<< HEAD
		request.session.save()		

	def test_dummy(self):
		self.assertEqual(1,1)				

	def test_view_ok(self):
		request = self.factory.get('/calendario/evento/altera/')
		self.setup_request(request)
		request.user = self.user
		evento = EventoFactory.create()
		response = EventoUpdate.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/evento/update.html')


class EventoCreateTest(TestCase):

=======
		request.session.save()

	def test_dummy(self):
		self.assertEqual(1,1)		

	def test_view_ok(self):
		request = self.factory.get('/calendario/evento/')
		self.setup_request(request)
		response = EventoIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						
		self.assertEqual(response.template_name[0], 'calendario/evento/index.html')

class EventoUpdateTest(TestCase):
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
<<<<<<< HEAD
=======
		self.user.is_superuser = True
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60
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
<<<<<<< HEAD
		request = self.factory.get('/calendario/evento/novo/')
		self.setup_request(request)
		response = EventoIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						
>>>>>>> issue31
=======
		request = self.factory.get('/calendario/evento/altera/')
		self.setup_request(request)
		request.user = self.user
		evento = EventoFactory.create()
		response = EventoUpdate.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/evento/update.html')		
>>>>>>> 264607f53d869df49c27faee00f73d7adcaddb60
