# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Cliente(models.Model):
	nome = models.CharField(verbose_name = 'Nome', max_length = 100)
	cpf = models.CharField(verbose_name = 'CPF', max_length = 11)
	tipo = models.CharField(verbose_name = 'Tipo de Usúario', max_length = 1)
	celular = models.CharField(verbose_name = 'Número do Celular', max_length = 30)
	email = models.CharField(verbose_name = 'Email', max_length = 50)
	usuario = models.CharField(verbose_name = 'Usuário', max_length = 50)
	endereco = models.CharField(verbose_name = 'Endereço', max_length = 150)
	numero = models.CharField(verbose_name = 'Número', max_length = 11)
	estado = models.CharField(verbose_name = 'Estado', max_length = 1)
	cep = models.CharField(verbose_name = 'Cep', max_length = 8)
	senha = models.CharField(verbose_name = 'Senha', max_length = 50)
	foto = models.ImageField(upload_to='cliente/', height_field=None, width_field=None, max_length=100,blank=True,null=True,default='cliente/no_foto.jpg')
	cliente = models.Manager()
