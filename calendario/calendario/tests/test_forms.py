# -*- coding: utf-8 -*-

from django.test import TestCase, Client, RequestFactory
from django.db import IntegrityError, DataError
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime

from ..forms import LocalForm

class LocalFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user('zaquinha', password='zaca')
        self.user.is_staff = True
        self.user.lotado = 171
        self.user.matricula = 2179
        self.user.save()
        self.factory = RequestFactory()

    def test_init(self):
        form = LocalForm()

