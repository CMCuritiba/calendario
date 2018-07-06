from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from autentica.models import User

from ..views import CalendarioIndex, CalendarioEventoDetails, LocalIndex, LocalCreate, LocalUpdate, EventoIndex, EventoUpdate, ComunicadoIndex, ComunicadoCreate, ComunicadoUpdate
from ..factories import EventoFactory, LocalFactory, ComunicadoFactory

#--------------------------------------------------------------------------------------
# Teste view index calendario
#--------------------------------------------------------------------------------------
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
		self.assertEqual(response.template_name[0], 'calendario/index.html')

#--------------------------------------------------------------------------------------
# Teste view detalhes calendario
#--------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------
# Teste view inicial local
#--------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------
# Teste view criacao local
#--------------------------------------------------------------------------------------
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


#--------------------------------------------------------------------------------------
# Teste view alteracao local
#--------------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------------
# Teste view inicial evento
#--------------------------------------------------------------------------------------
class EventoIndexTest(TestCase):
	
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
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()		

	def test_dummy(self):
		self.assertEqual(1,1)				

	def test_view_ok(self):
		request = self.factory.get('/calendario/evento/')
		self.setup_request(request)
		request.user = self.user
		response = EventoIndex.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/evento/index.html')


#--------------------------------------------------------------------------------------
# Teste view criacao evento
#--------------------------------------------------------------------------------------
class EventoCreateTest(TestCase):

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
		request.session.save()

		middleware = MessageMiddleware()
		middleware.process_request(request)
		request.session.save()		
	
	def test_view_ok(self):
		request = self.factory.get('/calendario/evento/')
		self.setup_request(request)
		response = EventoIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						
		self.assertEqual(response.template_name[0], 'calendario/evento/index.html')

#--------------------------------------------------------------------------------------
# Teste view atualizacao evento
#--------------------------------------------------------------------------------------
class EventoUpdateTest(TestCase):
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
		request = self.factory.get('/calendario/evento/altera/')
		self.setup_request(request)
		request.user = self.user
		evento = EventoFactory.create()
		response = EventoUpdate.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/evento/update.html')

#--------------------------------------------------------------------------------------
# Teste view inicial comunicado
#--------------------------------------------------------------------------------------
class ComunicadoIndexTest(TestCase):
	
	nome_usuario = 'zaca'
	senha = 'nosferatu'

	def setUp(self):
		self.user = get_user_model().objects.create_user(self.nome_usuario, password=self.senha)
		self.user.is_staff = True
		self.user.save()
		self.factory = RequestFactory()
		comunicado = ComunicadoFactory()

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
		request = self.factory.get('/calendario/comunicado/index/')
		self.setup_request(request)
		response = ComunicadoIndex.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						

#--------------------------------------------------------------------------------------
# Teste view criacao comunicado
#--------------------------------------------------------------------------------------
class ComunicadoCreateTest(TestCase):

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
		request = self.factory.get('/calendario/comunicado/novo/')
		self.setup_request(request)
		response = ComunicadoCreate.as_view()(request)
		response.render()
		self.assertEqual(response.status_code, 200)						

#--------------------------------------------------------------------------------------
# Teste view alteracao comunicado
#--------------------------------------------------------------------------------------
class ComunicadoUpdateTest(TestCase):
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
		request = self.factory.get('/calendario/comunicado/altera/')
		self.setup_request(request)
		request.user = self.user
		comunicado = ComunicadoFactory.create()
		response = ComunicadoUpdate.as_view()(request, pk=1)
		response.render()
		self.assertEqual(response.status_code, 200)								
		self.assertEqual(response.template_name[0], 'calendario/comunicado/update.html')