# associados/forms.py
from django import forms
from .models import *

class AssociadoForm(forms.ModelForm):
    class Meta:
        model = Associado
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }  

class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        exclude = ['socio_titular']
        widgets = {
                'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            }  

class EspacoForm(forms.ModelForm):
    class Meta:
        model = EspacoLocavel
        fields = '__all__'
        widgets = {
                'data_construcao_aquisicao': forms.DateInput(attrs={'type': 'date'}),
            }  

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = '__all__'

class ConvidadoForm(forms.ModelForm):
    class Meta:
        model = Convidado
        fields = '__all__'

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ['convidados']
        widgets = {
            'data_hora_inicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_hora_fim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


