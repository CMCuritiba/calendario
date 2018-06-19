# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, CharField, DecimalField, DateField, BooleanField
from django.forms.models import inlineformset_factory
from django.forms import formsets, models
from django.forms.models import modelformset_factory
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, Button, HTML, ButtonHolder
from crispy_forms.bootstrap import (PrependedText, PrependedAppendedText, FormActions, AppendedText)
from crispy_forms.bootstrap import StrictButton
from django.conf import settings
from decimal import Decimal

from django.contrib.sessions.backends.db import SessionStore

from calendario.calendario.models import Evento, Local

#------------------------------------------------------------------------------------------
# classe form utilizada para validar JSON de alteração de status dos locais
#------------------------------------------------------------------------------------------
class JSONLocalForm(forms.Form):

	def __init__(self, *args, **kwargs):
		super(JSONLocalForm, self).__init__(*args, **kwargs)

		self.fields['pk'] = forms.IntegerField()

#------------------------------------------------------------------------------------------
# classe form para manutenção de locais
#------------------------------------------------------------------------------------------
class LocalForm(forms.ModelForm):

    class Meta:
        model = Local
        fields = ['local', 'status']

    def __init__(self, *args, **kwargs):
        super(LocalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.layout = Layout(
            Div(
                Div('local', css_class='col-md-12',),
                css_class='col-md-12 row',
            ),
            Div(
                Div('status', css_class='col-md-12',),
                css_class='col-md-3 row',
            ),
        )		