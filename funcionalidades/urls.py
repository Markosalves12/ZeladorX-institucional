from django.urls import path
from funcionalidades.views import (gestao_de_equipes, plano_de_melhorias, macro_servicos, automacoes, agendamentos,
                                   relatorios_planejamento, relatorios_de_comprovacao)

urlpatterns = [
    path('funcionalidades/gestao-de-equipes/', gestao_de_equipes, name='gestao_de_equipes'),
    path('funcionalidades/plano-de-melhorias/', plano_de_melhorias, name='plano_de_melhorias'),
    path('funcionalidades/macro-servicos/', macro_servicos, name='macro_servicos'),
    path('funcionalidades/automacoes/', automacoes, name='automacoes'),
    path('funcionalidades/agendamentos/', agendamentos, name='agendamentos'),
    path('funcionalidades/relatorios-de-planejamento/', relatorios_planejamento, name='relatorios_planejamento'),
    path('funcionalidades/relatorios-de-comprovacao/', relatorios_de_comprovacao, name='relatorios_de_comprovacao'),
]