# Mantenha o AtivoForm que você já tem e adicione estes:
from django import forms
from .models import Ativo, ManutencaoProgramada, OrdemServico

# Formulário que você já tem (apenas para referência)
class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = '__all__'
        widgets = {
            'data_fabricacao': forms.DateInput(attrs={'type': 'date'}),
            'data_aquisicao': forms.DateInput(attrs={'type': 'date'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

# NOVO: Formulário para Manutenção Programada
class ManutencaoProgramadaForm(forms.ModelForm):
    class Meta:
        model = ManutencaoProgramada
        fields = ['ativo', 'data_programada', 'tipo_manutencao', 'servico', 'status', 'observacao']
        widgets = {
            'ativo': forms.Select(attrs={'class': 'form-select'}),
            'data_programada': forms.DateInput(attrs={'type': 'date'}),
            'tipo_manutencao': forms.Select(attrs={'class': 'form-select'}),
            'servico': forms.TextInput(attrs={'placeholder': 'Ex: Troca de óleo do motor'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

# NOVO: Formulário para Ordem de Serviço
class OrdemServicoForm(forms.ModelForm):
    class Meta:
        model = OrdemServico
        # O campo 'data' é auto_now_add, então não incluímos no form
        fields = ['ativo', 'manutencao_origem', 'servico', 'hodometro_atual', 'horimetro_atual', 'observacao']
        widgets = {
            'ativo': forms.Select(attrs={'class': 'form-select'}),
            'manutencao_origem': forms.Select(attrs={'class': 'form-select'}),
            'servico': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva os serviços realizados...'}),
            'hodometro_atual': forms.NumberInput(attrs={'step': '0.1'}),
            'horimetro_atual': forms.NumberInput(attrs={'step': '0.1'}),
            'observacao': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Torna o campo 'manutencao_origem' opcional no formulário
        self.fields['manutencao_origem'].required = False
        # Filtra as manutenções de origem para mostrar apenas as do ativo selecionado (se houver)
        # Esta é uma funcionalidade mais avançada que pode ser implementada com JavaScript (htmx, etc.)
        # Por enquanto, mostramos todas.