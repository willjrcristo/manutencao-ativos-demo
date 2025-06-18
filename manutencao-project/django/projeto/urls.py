"""
URL configuration for manutencao_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# No início, adicione as novas views que você criou
from manutencao_app.views import (
    viewDashboard, 
    listViewAtivos, createViewAtivo, updateViewAtivo, deleteViewAtivo,
    listViewManutencoes, createViewManutencao, updateViewManutencao, deleteViewManutencao,
    listViewOrdensServico, createViewOrdemServico, updateViewOrdemServico, deleteViewOrdemServico
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Raiz
    path('', viewDashboard, name='dashboard'),

    # Rotas para Ativos (já existentes)
    path('ativos/', listViewAtivos, name='ativo_list'),
    path('ativos/novo/', createViewAtivo.as_view(), name='ativo_create'),
    path('ativos/<int:pk>/editar/', updateViewAtivo.as_view(), name='ativo_update'),
    path('ativos/<int:pk>/excluir/', deleteViewAtivo.as_view(), name='ativo_delete'),
    
    # NOVAS: Rotas para Manutenção Programada
    path('manutencoes/', listViewManutencoes, name='manutencao_list'),
    path('manutencoes/nova/', createViewManutencao.as_view(), name='manutencao_create'),
    path('manutencoes/<int:pk>/editar/', updateViewManutencao.as_view(), name='manutencao_update'),
    path('manutencoes/<int:pk>/excluir/', deleteViewManutencao.as_view(), name='manutencao_delete'),
    
    # NOVAS: Rotas para Ordem de Serviço
    path('ordens-servico/', listViewOrdensServico, name='ordem_servico_list'),
    path('ordens-servico/nova/', createViewOrdemServico.as_view(), name='ordem_servico_create'),
    path('ordens-servico/<int:pk>/editar/', updateViewOrdemServico.as_view(), name='ordem_servico_update'),
    path('ordens-servico/<int:pk>/excluir/', deleteViewOrdemServico.as_view(), name='ordem_servico_delete'),
]