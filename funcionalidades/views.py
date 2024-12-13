from django.shortcuts import render
from funcionalidades.utils_equipes import (overview_equipes, individuali_permission,
                                           productivity, escales, organization, how_functions, dashboards)
from funcionalidades.utils_macro_services import macro_service_jardinagem, macro_limpeza_predial, reports, report_comprovation
from funcionalidades.utils_limpeza_predial import automacoes_limpeza_predial_description, agendamentos_limpeza_predial_description
from funcionalidades.utils_jardinagem import automacoes_jardinagem_description, agendamentos_jardinagem_description
from funcionalidades.utils_reports import (relatorio_planejamento_xlsx_jardinagem,
                                           relatorio_planejamento_xlsx_limpeza_predial,
                                           relatorio_planejamento_pdf_jardinagem,
                                           relatorio_planejamento_pdf_limpeza_predial,
                                           relatorio_comprovacao_xlsx_jardinagem,
                                           relatorio_comprovacao_xlsx_limpeza_predial,
                                           relatorio_comprovacao_pdf_jardinagem,
                                           relatorio_comprovacao_pdf_limpeza_predial)
from utils.views import generic_view


# Create your views here.
def gestao_de_equipes(request):
    contents = [
        {
            'type': 'card-left-tabs',
            'title_card': 'Gestao de equipes',
            'id': 2,
            'tabs_title_contents': {
                'Visao geral das equipes': [overview_equipes],
                'Permissões individuais': [individuali_permission],
                'Acompanhamento de desempenho': [productivity],
                'Controle de membros e supervisores': [organization],
                'Organização de escalas': [escales],
            }
        },
        {
            'type': 'card-no-tabs',
            'title_card': 'Como Funciona na Prática',
            'texts': how_functions,
        }
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Gestão de Equipes',
        page_name='Gestão de Equipes',
        description='Organize, monitore e otimize a performance das suas equipes.',
    )


def macro_servicos(request):
    contents = [
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Macro servicos',
            'tabs_title_contents': {
                'Jardinagem': [macro_service_jardinagem],
                'Limpeza predial': [macro_limpeza_predial],
            }
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Macro serviços de todas as carteiras',
        page_name='Macro Serviços',
        description='Simplifique e automatize a gestão de serviços de grande escala com o ZeladorX.',
    )

def automacoes(request):
    contents = [
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Automações',
            'tabs_title_contents': {
                'Jardinagem': [automacoes_jardinagem_description],
                'Limpeza predial': [automacoes_limpeza_predial_description],
            }
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Automações Inteligentes para Serviços de Excelência',
        page_name='Automações',
        description='ZeladorX traz o poder da automação para otimizar o desempenho e a qualidade dos seus serviços.',
    )


def agendamentos(request):
    contents = [
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Esquema de agendamentos',
            'tabs_title_contents': {
                'Jardinagem': [agendamentos_jardinagem_description],
                'Limpeza predial': [agendamentos_limpeza_predial_description],
            }
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Agendamentos Inteligentes para Serviços de Excelência',
        page_name='Agendamentos',
        description='ZeladorX traz o poder da automação para otimizar o desempenho e a qualidade dos seus serviços.',
    )


def relatorios_planejamento(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Os relatórios de planejamento do zeladorX',
            'texts': reports
        },
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Relatórios de serviços planejados XLSX (Excel)',
            'tabs_title_contents': {
                'Jardinagem': [relatorio_planejamento_xlsx_jardinagem,],
                'Limpeza predial': [relatorio_planejamento_xlsx_limpeza_predial],
            }
        },
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Relatórios planejados PDF',
            'tabs_title_contents': {
                'Jardinagem': [relatorio_planejamento_pdf_jardinagem, 'docs/documents/relatorio_de_servicos_Agendado_Em_andamento_jardinagem.pdf'],
                'Limpeza predial': [relatorio_planejamento_pdf_limpeza_predial, 'docs/documents/relatorio_de_servicos_Agendado_Em_andamento_limpeza_predial.pdf'],
            }
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Relatórios Inteligentes: PDF e Excel para Gestão Eficiente',
        page_name='Relatórios',
        description='Com o ZeladorX, obtenha relatórios detalhados e personalizáveis em PDF e Excel, otimizando a '
                      'tomada de decisões e a análise de desempenho.'
    )


def relatorios_de_comprovacao(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Os relatórios de comprovação do zeladorX',
            'texts': report_comprovation
        },
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Relatórios de serviços concluídos XLSX (Excel)',
            'tabs_title_contents': {
                'Jardinagem': [relatorio_comprovacao_xlsx_jardinagem,],
                'Limpeza predial': [relatorio_comprovacao_xlsx_limpeza_predial],
            }
        },
        {
            'type': 'card-left-tabs',
            'id': 3,
            'title_card': 'Relatórios de compravação PDF',
            'tabs_title_contents': {
                'Jardinagem': [relatorio_comprovacao_pdf_jardinagem, 'docs/documents/relatorio_de_servicos_Concluido_jardinagem.pdf'],
                'Limpeza predial': [relatorio_comprovacao_pdf_limpeza_predial, 'docs/documents/relatorio_de_servicos_Concluido_limpeza_predial.pdf'],
            }
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Relatórios Inteligentes: PDF e Excel para Gestão Eficiente',
        page_name='Relatórios',
        description='Com o ZeladorX, obtenha relatórios detalhados e personalizáveis em PDF e Excel, otimizando a '
                      'tomada de decisões e a análise de desempenho.'
    )

def plano_de_melhorias(request):
    contents = [
        {
            'type': 'pdf-reader',
            'title_card': 'Documentação',
            'doc_walk': 'docs/documents/Plano_de_melhorias.pdf'
        }
    ]

    return render(
        request=request,
        context={
            'page_title': 'Plano de Melhorias: Inovação e Inteligência para Serviços Eficientes',
            'page_name': 'Plano de Melhorias:',
            'description': 'Com o ZeladorX, impulsione a qualidade de seus serviços com tecnologia '
                           'avançada e insights estratégicos.',
            'contents': contents
        },
        template_name='new_index.html'
    )
