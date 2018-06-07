# -*- coding: utf-8 -*-

from django.apps import AppConfig


class CalendarioConfig(AppConfig):
    name = 'calendario.calendario'
    verbose_name = "CALENDARIO"

    def ready(self):
        pass
