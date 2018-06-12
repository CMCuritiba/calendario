# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError

from datetime import datetime

class Entry(models.Model):
    ident = models.IntegerField()
    local = models.CharField(max_length=300)
    status = models.CharField(max_length=1)

    def __str__(self):
        return self.local
