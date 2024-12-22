from django.shortcuts import render
from suporte.utils_FAQ import (introduction_to_zx, setting_firs_steps, manager_scalles, schedules_tasks,
                               reports_indicator, securuty_privacy, suport_to_client)
from suporte.forms import Contact
from utils.utils import enviar_notificacao
from django.contrib import messages
from django.shortcuts import reverse

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
            'url': reverse('contato'),
            'forms': Contact()
        }
    ]

    if request.method == 'POST':
        forms = Contact(request.POST)

        if forms.is_valid():
            email = forms['email'].value()
            nome = forms['nome'].value()
            assunto = forms['assunto'].value()
            menssagem = forms['Mensagem'].value()

            enviar_notificacao(
                destinatario=[email],
                assunto=assunto,
                contexto={
                    'nome': nome,
                    'email': email,
                    'menssagem': menssagem
                },
                template='notifications/send_message.html'
            )

            messages.success(request, "Mensagem recebida pelo nosso time")


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
