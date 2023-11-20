from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Associado, Dependente, EspacoLocavel, Fornecedor, Convidado, Agenda
from .forms import *
from django.urls import reverse_lazy

# views do associado

def Index(request):
    return render(request, 'index.html')

class AssociadoListView(ListView):
    model = Associado
    template_name = 'associado/associado_list.html'

class AssociadoDetailView(DetailView):
    model = Associado
    template_name = 'associado/associado_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dependentes'] = self.object.dependentes.all()
        return context

class AssociadoCreateView(CreateView):
    model = Associado
    form_class = AssociadoForm
    template_name = 'associado/associado_form.html'
    success_url = '/associados/'

class AssociadoUpdateView(UpdateView):
    model = Associado
    form_class = AssociadoForm
    template_name = 'associado/associado_edit.html'

    def get_success_url(self):
        return reverse_lazy('associado_detail', kwargs={'pk': self.object.pk})
    
class AssociadoDeleteView(DeleteView):
    model = Associado
    success_url = reverse_lazy('associado_list')

# views do dependente

class DependenteDetailView(DetailView):
    model = Dependente
    template_name = 'dependente/dependente_detail.html'

class DependenteCreateView(CreateView):
    model = Dependente
    form_class = DependenteForm
    template_name = 'dependente/dependente_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['associado_id'] = self.kwargs['associado_id']
        return context

    def form_valid(self, form):
        form.instance.socio_titular_id = self.kwargs['associado_id']
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('associado_detail', kwargs={'pk': self.kwargs['associado_id']})
    
class DependenteUpdateView(UpdateView):
    model = Dependente
    form_class = DependenteForm
    template_name = 'dependente/dependente_edit.html'

    def get_success_url(self):
        return reverse_lazy('dependente_detail', kwargs={'pk': self.object.pk})
    
class DependenteDeleteView(DeleteView):
    model = Dependente

    def get_success_url(self):
        return reverse_lazy('associado_detail', kwargs={'pk': self.object.socio_titular.pk})

    
    
# views do espaco locavel

class EspacoListView(ListView):
    model = EspacoLocavel
    template_name = 'espaco/espaco_list.html'

class EspacoCreateView(CreateView):
    model = EspacoLocavel
    form_class = EspacoForm
    template_name = 'espaco/espaco_form.html'
    success_url = reverse_lazy('espaco_list')

class EspacoUpdateView(UpdateView):
    model = EspacoLocavel
    form_class = EspacoForm
    template_name = 'espaco/espaco_edit.html'

    def get_success_url(self):
        return reverse_lazy('espaco_list')
    
class EspacoDeleteView(DeleteView):
    model = EspacoLocavel
    success_url = reverse_lazy('espaco_list')

# views do fornecedor

class FornecedorListView(ListView):
    model = Fornecedor
    template_name = 'fornecedor/fornecedor_list.html'

class FornecedorDetailView(DetailView):
    model = Fornecedor
    template_name = 'fornecedor/fornecedor_detail.html'

class FornecedorCreateView(CreateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor/fornecedor_form.html'
    success_url = reverse_lazy('fornecedor_list')

class FornecedorUpdateView(UpdateView):
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor/fornecedor_edit.html'

    def get_success_url(self):
        return reverse_lazy('fornecedor_detail', kwargs={'pk': self.object.pk})

class FornecedorDeleteView(DeleteView):
    model = Fornecedor
    success_url = reverse_lazy('fornecedor_list')
    

#views do convidado

class ConvidadoCreateView(CreateView):
    model = Convidado
    form_class = ConvidadoForm
    template_name = 'convidado/convidado_form.html'
    def get_success_url(self):
        return reverse_lazy('convidado_cadastrar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_convidados'] = Convidado.objects.all()
        return context
    
class ConvidadoListView(ListView):
    model = Convidado
    template_name = 'convidado/convidado_list.html'

class ConvidadoUpdateView(UpdateView):
    model = Convidado
    form_class = ConvidadoForm
    template_name = 'convidado/convidado_edit.html'

    def get_success_url(self):
        return reverse_lazy('convidado_list')
    
class ConvidadoDeleteView(DeleteView):
    model = Convidado
    success_url = reverse_lazy('convidado_list')

#views da agenda

class AgendaListView(ListView):
    model = Agenda
    template_name = 'agenda/agenda_list.html'

class AgendaDetailView(DetailView):
    model = Agenda
    template_name = 'agenda/agenda_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['convidados'] = self.object.convidados.all()
        return context

class AgendaUpdateView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda/agenda_edit.html'
    success_url = reverse_lazy('agenda_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['existing_convidados'] = Convidado.objects.all()
        return context
    
class AgendaDeleteView(DeleteView):
    model = Agenda
    success_url = reverse_lazy('agenda_list')

def agenda_cadastrar(request):
    if request.method == 'POST':
        agenda_form = AgendaForm(request.POST)
        if agenda_form.is_valid():
            agenda = agenda_form.save(commit=False)
            agenda.save()
            return redirect('add_convidados', agenda_id=agenda.id)
    else:
        agenda_form = AgendaForm()

    return render(request, 'agenda/agenda_form.html', {'agenda_form': agenda_form})

def add_convidados(request, agenda_id):
    agenda = Agenda.objects.get(id=agenda_id)

    if request.method == 'POST':
        # Processar form com convidados selecionados
        selected_convidados = request.POST.getlist('convidados')
        agenda.convidados.set(selected_convidados)
        return redirect('agenda_list')  

    # Fetch dos convidados existentes para seleção
    existing_convidados = Convidado.objects.all()
    convidado_form = ConvidadoForm()

    return render(request, 'agenda/agenda_convidados.html', {'convidado_form': convidado_form, 'agenda': agenda, 'existing_convidados': existing_convidados})


def edit_convidados(request, agenda_id):
    agenda = Agenda.objects.get(id=agenda_id)

    if request.method == 'POST':
        selected_convidados = request.POST.getlist('convidados')
        agenda.convidados.set(selected_convidados)
        return redirect('agenda_list')

    existing_convidados = Convidado.objects.all()
    convidado_form = ConvidadoForm()

    return render(request, 'agenda/agenda_edit_convidados.html', {'convidado_form': convidado_form, 'agenda': agenda, 'existing_convidados': existing_convidados})