from django.urls import path
from .views import *

urlpatterns = [
    # index
    path('', Index, name='index'),

    # urls do associado

    path('associados/', AssociadoListView.as_view(), name='associado_list'),
    path('associados/<int:pk>/', AssociadoDetailView.as_view(), name='associado_detail'),
    path('associados/cadastrar/', AssociadoCreateView.as_view(), name='associado_cadastrar'),
    path('associados/<int:pk>/editar/', AssociadoUpdateView.as_view(), name='associado_edit'),
    path('associados/<int:pk>/excluir/', AssociadoDeleteView.as_view(), name='associado_delete'),

    # urls do dependente

    path('associados/<int:associado_id>/dependentes/<int:pk>/', DependenteDetailView.as_view(), name='dependente_detail'),
    path('associados/<int:associado_id>/dependentes/cadastrar/', DependenteCreateView.as_view(), name='dependente_cadastrar'),
    path('associados/<int:associado_id>/dependentes/<int:pk>/editar/', DependenteUpdateView.as_view(), name='dependente_edit'),
    path('dependentes/<int:pk>/excluir/', DependenteDeleteView.as_view(), name='dependente_delete'),

    # urls do espaco

    path('espacos/', EspacoListView.as_view(), name='espaco_list'),
    path('espacos/cadastrar/', EspacoCreateView.as_view(), name='espaco_cadastrar'),
    path('espacos/<int:pk>/editar/', EspacoUpdateView.as_view(), name='espaco_edit'),
    path('espacos/<int:pk>/excluir/', EspacoDeleteView.as_view(), name='espaco_delete'),

    # urls do fornecedor

    path('fornecedores/', FornecedorListView.as_view(), name='fornecedor_list'),
    path('fornecedores/cadastrar/', FornecedorCreateView.as_view(), name='fornecedor_cadastrar'),
    path('fornecedores/<int:pk>/', FornecedorDetailView.as_view(), name='fornecedor_detail'),
    path('fornecedores/<int:pk>/editar/', FornecedorUpdateView.as_view(), name='fornecedor_edit'),
    path('fornecedores/<int:pk>/excluir/', FornecedorDeleteView.as_view(), name='fornecedor_delete'),

    # urls da agenda

    path('agenda/', AgendaListView.as_view(), name='agenda_list'),
    path('convidados/cadastrar/', ConvidadoCreateView.as_view(), name='convidado_cadastrar'),
    path('agenda/cadastrar/', agenda_cadastrar, name='agenda_cadastrar'),
    path('agenda/<int:agenda_id>/add_convidados/', add_convidados, name='add_convidados'),
    path('agenda/<int:pk>/edit/', AgendaUpdateView.as_view(), name='agenda_edit'),
    path('agenda/<int:agenda_id>/edit_convidados/', edit_convidados, name='edit_convidados'),
    path('agenda/<int:pk>/', AgendaDetailView.as_view(), name='agenda_detail'),
    path('agenda/<int:pk>/excluir/', AgendaDeleteView.as_view(), name='agenda_delete'),

    # urls de convidados

    path('convidados/', ConvidadoListView.as_view(), name='convidado_list'),
    path('convidados/<int:pk>/excluir/', ConvidadoDeleteView.as_view(), name='convidado_delete'),
    path('convidados/<int:pk>/editar/', ConvidadoUpdateView.as_view(), name='convidado_edit'),
    # Repita o mesmo padrão para outros modelos
]
