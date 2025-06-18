# Em manutencao_app/forms.py

from django import forms
from .models import Ativo # Importa o modelo que servirá de base

class AtivoForm(forms.ModelForm):
    class Meta:
        model = Ativo
        fields = [
            'descricao', 
            'tipo_ativo', 
            'data_aquisicao',
            'observacao'
        ]
        
        widgets = {
            'descricao': forms.TextInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm',
                'placeholder': 'Descreva o ativo detalhadamente'
            }),
            'tipo_ativo': forms.Select(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 bg-white rounded-md shadow-sm'
            }),
            'data_aquisicao': forms.DateInput(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm',
                'type': 'date'  # Garante que o navegador mostre um seletor de data
            }),
            'observacao': forms.Textarea(attrs={
                'class': 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm',
                'rows': 3 # Define a altura da área de texto
            }),
        }