# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.models import User
from loja.models import *
from django.template import RequestContext
# Create your views here.
def index(request):
	try:
		if request.session['usuario'] == '':
			request.session['usuario'] = ''
	except:
		request.session['usuario'] = ''

	return render(request,'index.html',{
		'usuario': request.session['usuario']

		})
def entrar(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']	

		return render(request,'entrar.html',{'s': usuario})

	return render(request,'entrar.html',{
		'usuario': request.session['usuario']

		})
def cadastro(request):
	if request.method == 'POST':
		nome = request.POST['nome']
		usuario = request.POST['usuario']
		cpf = request.POST['cpf']
		endereco = request.POST['endereco']
		numero = request.POST['numero']
		estado = request.POST['estado']
		celular = request.POST['celular']
		cep = request.POST['cep']
		tipo = request.POST['tipo']
		email = request.POST['email']
		senha = request.POST['senha']
		c = Cliente.cliente.create(nome=nome, cpf=cpf, usuario=usuario, endereco=endereco, numero=numero, estado=estado, celular=celular, cep=cep, tipo=tipo, email=email, senha=senha,)
		c.save()
		return render(request,'cadastro.html',{})		
	return render(request,'cadastro.html',{})
