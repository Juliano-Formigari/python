"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testeView.views import retornaRequest, exibeTabela, Inicio, Contato
from Pessoa.views import lista_tp_pessoa, lista_fornecedores, lista_clientes, lista_usuarios
from Pessoa.views import cadastra_tp_pessoa, cadastra_fornecedor, cadastra_cliente, cadastra_usuario
from Pessoa.views import altera_tp_pessoa, altera_fornecedor, altera_cliente, altera_usuario
from Item.views import lista_categorias, lista_itens
from Item.views import cadastra_categoria, cadastra_item
from Item.views import altera_categoria, altera_item
from Local.views import lista_cidades, lista_estados
from Local.views import cadastra_cidade, cadastra_estado
from Local.views import altera_cidade, altera_estado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__exemplo', retornaRequest),
    path('__tabela', exibeTabela),
    path('inicio', Inicio),
    path('contato', Contato),
    path('lista-tipos-pessoa', lista_tp_pessoa),
    path('cadastra_tp_pessoa', cadastra_tp_pessoa),
    path('altera_tp_pessoa', altera_tp_pessoa),
    path('lista-fornecedores', lista_fornecedores),
    path('cadastra_fornecedor', cadastra_fornecedor),
    path('altera_fornecedor', altera_fornecedor),
    path('lista-clientes', lista_clientes),
    path('cadastra_cliente', cadastra_cliente),
    path('altera_cliente', altera_cliente),
    path('lista-usuarios', lista_usuarios),
    path('cadastra_usuario', cadastra_usuario),
    path('altera_usuario', altera_usuario),
    path('lista-categorias', lista_categorias),
    path('cadastra_categoria', cadastra_categoria),
    path('altera_categoria', altera_categoria),
    path('lista-itens', lista_itens),
    path('cadastra_item', cadastra_item),
    path('altera_item', altera_item),
    path('lista-cidades', lista_cidades),
    path('cadastra_cidade', cadastra_cidade),
    path('altera_cidade', altera_cidade),
    path('lista-estados', lista_estados),
    path('cadastra_estado', cadastra_estado),
    path('altera_estado', altera_estado),
    path('', Inicio),
]
