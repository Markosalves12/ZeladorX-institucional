from django.shortcuts import render
from suporte.utils_FAQ import (introduction_to_zx, setting_firs_steps, manager_scalles, schedules_tasks,
                               reports_indicator, securuty_privacy, suport_to_client)

# Create your views here.
def FAQ(request):
    contents = [
        {
            'type': 'awser-responses',
            'title_card': '',
            'tabs_title_contents': {
                '1. Introdução ao ZeladorX': ['collapseOne', 'collapse show', introduction_to_zx],
                '2. Configuração e Primeiros Passos': ['collapseTwo', 'collapse show', setting_firs_steps],
                '3. Gerenciamento de Equipes e Escalas': ['collapseThree', 'collapse show', manager_scalles],
                '4. Agendamento de Tarefas e Serviços': ['collapseFour', 'collapse show', schedules_tasks],
                '5. Relatórios e Indicadores de Desempenho': ['collapseFive', 'collapse show', reports_indicator],
                '6. Segurança e Privacidade': ['collapseSix', 'collapse show', securuty_privacy],
                '7. Suporte e Atendimento ao Cliente': ['collapseSeven', 'collapse show', suport_to_client],
            }
        },
    ]

    return render(
        request=request,
        context={
            'page_title': 'Perguntas frequentes',
            'page_name': 'FAQ',
            'desciption': 'Simplifique operações e potencialize a produtividade com o ZeladorX.',
            'contents': contents
        },
        template_name='new_index.html'
    )

def contato(request):
    contents = [
        {
            'type': 'contact',
            'title_card': '',
            'tabs_title_contents': {
                '1. Introdução ao ZeladorX': ['collapseOne', 'collapse show', introduction_to_zx],
                '2. Configuração e Primeiros Passos': ['collapseTwo', 'collapse', setting_firs_steps],
                '3. Gerenciamento de Equipes e Escalas': ['collapseThree', 'collapse', manager_scalles],
                '4. Agendamento de Tarefas e Serviços': ['collapseFour', 'collapse', schedules_tasks],
                '5. Relatórios e Indicadores de Desempenho': ['collapseFive', 'collapse', reports_indicator],
                '6. Segurança e Privacidade': ['collapseSix', 'collapse', securuty_privacy],
                '7. Suporte e Atendimento ao Cliente': ['collapseSeven', 'collapse', suport_to_client],
            }
        },
    ]

    return render(
        request=request,
        context={
            'page_title': 'Contato',
            'page_name': 'Contato',
            'desciption': 'Precisa de um contato direto com nosso time',
            'contents': contents
        },
        template_name='new_index.html'
    )
