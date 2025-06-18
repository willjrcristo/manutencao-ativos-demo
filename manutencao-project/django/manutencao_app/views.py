# No arquivo views.py do seu app
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ativo, ManutencaoProgramada, OrdemServico
from .forms import AtivoForm, ManutencaoProgramadaForm, OrdemServicoForm

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

# ===============================================
# VIEWS PARA MANUTENÇÃO PROGRAMADA
# ===============================================

def listViewManutencoes(request):
    query = request.GET.get('q')
    
    if query:
        # Busca por serviço ou descrição do ativo
        manutencoes = ManutencaoProgramada.objects.filter(
            models.Q(servico__icontains=query) | 
            models.Q(ativo__descricao__icontains=query)
        ).select_related('ativo') # Otimiza a busca do ativo
    else:
        manutencoes = ManutencaoProgramada.objects.select_related('ativo').all()

    form = ManutencaoProgramadaForm()

    context = {
        'object_list': manutencoes,
        'form': form,
    }
    
    return render(request, 'manutencoes/manutencao_list.html', context)

class createViewManutencao(CreateView):
    model = ManutencaoProgramada
    form_class = ManutencaoProgramadaForm
    template_name = 'manutencoes/manutencao_form.html'
    success_url = reverse_lazy('manutencao_list')

class updateViewManutencao(UpdateView):
    model = ManutencaoProgramada
    form_class = ManutencaoProgramadaForm
    template_name = 'manutencoes/manutencao_form.html'
    success_url = reverse_lazy('manutencao_list')

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            self.object = self.get_object()
            form = self.get_form()
            return render(request, 'manutencoes/partials/manutencao_form_modal.html', {'form': form, 'object': self.object})
        return super().get(request, *args, **kwargs)

class deleteViewManutencao(DeleteView):
    model = ManutencaoProgramada
    template_name = 'manutencoes/manutencao_confirm_delete.html'
    success_url = reverse_lazy('manutencao_list')


# ===============================================
# VIEWS PARA ORDEM DE SERVIÇO
# ===============================================

def listViewOrdensServico(request):
    query = request.GET.get('q')
    
    if query:
        ordens = OrdemServico.objects.filter(
            models.Q(servico__icontains=query) | 
            models.Q(ativo__descricao__icontains=query)
        ).select_related('ativo')
    else:
        ordens = OrdemServico.objects.select_related('ativo').all()

    form = OrdemServicoForm()

    context = {
        'object_list': ordens,
        'form': form,
    }
    
    return render(request, 'ordens_servico/ordem_servico_list.html', context)

class createViewOrdemServico(CreateView):
    model = OrdemServico
    form_class = OrdemServicoForm
    template_name = 'ordens_servico/ordem_servico_form.html'
    success_url = reverse_lazy('ordem_servico_list')

class updateViewOrdemServico(UpdateView):
    model = OrdemServico
    form_class = OrdemServicoForm
    template_name = 'ordens_servico/ordem_servico_form.html'
    success_url = reverse_lazy('ordem_servico_list')

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            self.object = self.get_object()
            form = self.get_form()
            return render(request, 'ordens_servico/partials/ordem_servico_form_modal.html', {'form': form, 'object': self.object})
        return super().get(request, *args, **kwargs)

class deleteViewOrdemServico(DeleteView):
    model = OrdemServico
    template_name = 'ordens_servico/ordem_servico_confirm_delete.html'
    success_url = reverse_lazy('ordem_servico_list')