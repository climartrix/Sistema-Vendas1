"""Sistema_loja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','loja.views.index'),
    url(r'^entrar/$','loja.views.entrar', name='entrar_visual'),
    url(r'^Cadastro/','loja.views.cadastro', name='cadastro_visual'),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/',}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': './static/',}),
]

