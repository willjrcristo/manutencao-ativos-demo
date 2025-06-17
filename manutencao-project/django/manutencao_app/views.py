# No arquivo views.py do seu app
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ativo, ManutencaoProgramada, OrdemServico

def DashboardView(request):
    # Busca os dados (contagem) do banco de dados
    total_ativos = Ativo.objects.count()
    total_programacoes = ManutencaoProgramada.objects.count()
    total_os = OrdemServico.objects.count()

    # Cria o dicionário de contexto para enviar ao template
    context = {
        'total_ativos': total_ativos,
        'total_programacoes': total_programacoes,
        'total_os': total_os,
    }

    # Renderiza o template do dashboard, passando os dados
    return render(request, 'dashboard.html', context)

# View para listar todos os ativos
class AtivoListView(ListView):
    model = Ativo
    template_name = 'ativos/ativo_list.html'  # Template que vamos criar
    context_object_name = 'ativos'

# View para criar um novo ativo
class AtivoCreateView(CreateView):
    model = Ativo
    template_name = 'ativos/ativo_form.html'  # Template de formulário
    fields = '__all__'  # Usa todos os campos do modelo Ativo
    success_url = reverse_lazy('ativo_list') # Redireciona para a lista após sucesso

# View para atualizar um ativo existente
class AtivoUpdateView(UpdateView):
    model = Ativo
    template_name = 'ativos/ativo_form.html'
    fields = '__all__'
    success_url = reverse_lazy('ativo_list')

# View para deletar um ativo
class AtivoDeleteView(DeleteView):
    model = Ativo
    template_name = 'ativos/ativo_confirm_delete.html' # Template de confirmação
    success_url = reverse_lazy('ativo_list')