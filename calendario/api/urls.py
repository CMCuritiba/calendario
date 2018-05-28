# -*- coding: utf-8 -*-

from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'get_fake_calendario', views.FakeCalendarioViewSet, base_name='get_fake_calendario')

urlpatterns = [
]	

urlpatterns += router.urls
