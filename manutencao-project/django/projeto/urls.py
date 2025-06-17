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
from manutencao_app.views import AtivoListView, AtivoCreateView, AtivoUpdateView, AtivoDeleteView, DashboardView
# from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota para a raiz do site -> http://127.0.0.1:8000/
    path('', DashboardView, name='dashboard'),

    # Rota para a lista de ativos (Read)
    path('ativos/', AtivoListView.as_view(), name='ativo_list'),
    
    # Rota para o formulário de criação (Create)
    path('ativos/novo/', AtivoCreateView.as_view(), name='ativo_create'),
    
    # Rota para o formulário de edição (Update)
    path('ativos/<int:pk>/editar/', AtivoUpdateView.as_view(), name='ativo_update'),
    
    # Rota para a confirmação de exclusão (Delete)
    path('ativos/<int:pk>/excluir/', AtivoDeleteView.as_view(), name='ativo_delete'),
]
