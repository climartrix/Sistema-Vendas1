# -*- coding:utf-8 -*-
from django import forms
from django.forms import CharField, Form, PasswordInput,ModelForm
from django.contrib.admin import widgets         
from django.contrib.auth.models import User
from cadastro.models import *
from django.contrib.admin.widgets import AdminFileWidget
class FormLogin(forms.Form):
	usuario=forms.CharField(label='Usuário',required=True)
	senha=forms.CharField(label='Senha', required=True)


class FormLocalizaCliente(forms.Form):
	nome=forms.CharField(label='Nome', required=True,widget=forms.TextInput(attrs={'placeholder': 'Digite o nome para filtrar'}))

class FormFotoCliente(forms.Form):
	file = forms.FileField(label='Buscar foto')  

class FormCliente(ModelForm):
	class Meta:
		model=Cliente
		fields=['nome']

class FormLancamentoCliente(forms.Form):
	CD = (
	    ('Crédito', (
	            ('CD', 'Créditar'),
	            ('CE', 'Estornar Crédito'),
	        )
	    ),
	    ('Débito', (
	            ('DD', 'Débitar'),
	            ('DE', 'Estornar Débito'),
	        )
	    ),
	)

	cd = forms.ChoiceField(widget=forms.RadioSelect, choices=CD)
	valor = forms.DecimalField(label = 'Valor', max_digits = 15, decimal_places = 2, initial=0 ) 
	

