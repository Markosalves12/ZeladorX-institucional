from django.shortcuts import render
from aboutus.utils import mission, vision, ourvalues

# Create your views here.
def missao(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Missão',
            'texts': mission
        }
    ]

    return render(
        request=request,
        context={
            'page_title': 'Missão e Gestão Estratégica de Equipes',
            'page_name': 'Transformando Operações com Eficiência',
            'description': 'Gerencie, monitore e maximize a produtividade das suas equipes com soluções inovadoras.',
            'contents': contents
        },
        template_name='new_index.html'
    )


def visao(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Visão',
            'texts': vision
        }
    ]

    return render(
        request=request,
        context={
            'page_title': 'Visão e Estratégia Transformadora',
            'page_name': 'Liderando a Evolução na Gestão de Equipes',
            'description': 'Aspiramos ser referência global em inovação e eficiência, redefinindo padrões no gerenciamento de operações.',
            'contents': contents
        },
        template_name='new_index.html'
    )

def valores(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Valores',
            'texts': ourvalues
        }
    ]

    return render(
        request=request,
        context={
            'page_title': 'Nossos Valores',
            'page_name': 'Princípios Fundamentais',
            'description': 'Descubra os valores que sustentam nosso compromisso com a excelência e inovação.',
            'contents': contents
        },
        template_name='new_index.html'
    )