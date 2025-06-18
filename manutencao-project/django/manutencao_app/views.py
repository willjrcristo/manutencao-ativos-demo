# No arquivo views.py do seu app
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ativo, ManutencaoProgramada, OrdemServico
from .forms import AtivoForm 

def viewDashboard(request):
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
# class AtivoListView(ListView):
#     model = Ativo
#     template_name = 'ativos/ativo_list.html'  # Template que vamos criar
#     context_object_name = 'ativos'

def listViewAtivos(request):
    query = request.GET.get('q')
    
    if query:
        ativos = Ativo.objects.filter(descricao__icontains=query)
    else:
        ativos = Ativo.objects.all()

    # Crie uma instância vazia do formulário para ser usada no modal
    form = AtivoForm()

    context = {
        'object_list': ativos, # Mudei para object_list para consistência com CBVs
        'form': form, # Passe o formulário para o template
    }
    
    return render(request, 'ativos/ativo_list.html', context)

class createViewAtivo(CreateView):
    model = Ativo
    form_class = AtivoForm
    template_name = 'ativos/ativo_form.html'
    success_url = reverse_lazy('ativo_list')

class updateViewAtivo(UpdateView):
    model = Ativo
    form_class = AtivoForm
    template_name = 'ativos/ativo_form.html'
    success_url = reverse_lazy('ativo_list')

    def get(self, request, *args, **kwargs):
        # Verifica se a requisição é AJAX (feita pelo nosso modal)
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            self.object = self.get_object()
            form = self.get_form()
            # Renderiza apenas o fragmento do formulário
            return render(request, 'ativos/partials/ativo_form_modal.html', {'form': form, 'object': self.object})
        
        # Para requisições normais, continua com o comportamento padrão
        return super().get(request, *args, **kwargs)

# View para deletar um ativo
class deleteViewAtivo(DeleteView):
    model = Ativo
    template_name = 'ativos/ativo_confirm_delete.html' # Template de confirmação
    success_url = reverse_lazy('ativo_list')