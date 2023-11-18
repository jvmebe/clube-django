# associados/forms.py
from django import forms
from crispy_forms.layout import Layout, Submit, Field
from crispy_forms.helper import FormHelper
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


