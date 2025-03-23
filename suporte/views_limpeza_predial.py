from utils.views import generic_view

# Create your views here.
def manual_limpeza_predial(request):
    contents = [
        {
            'type': 'pdf-reader',
            'title_card': 'Manual de instruções',
            'doc_walk': 'docs/documents/Manual_ZX_limpeza_predial.pdf'
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Manual de Instruções - Macro Serviços de Limpeza predial',
        page_name='Documentação atualizada da carteira',
        description='Otimize a gestão de áreas verdes com o ZeladorX. Descubra como nossa tecnologia '
                    'inovadora e insights personalizados podem transformar os serviços de limpeza predial, '
                    'aumentando a eficiência e a qualidade.'
    )


def tutoriais_limpeza_predial(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Em desenvolvimento',
            'texts': "Em breve traremos tutoriais em video para melhor aprendizado dos nossos parceiros"
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Tutoriais do macro serviço de limpeza predial',
        page_name='Tutoriais',
        description='Explore nossos tutoriais em vídeo e aprenda a otimizar a gestão de áreas internas com o ZeladorX. '
                    'Descubra como nossa tecnologia inovadora pode transformar os serviços de limpeza, com instruções '
                    'claras e práticas que aumentam a eficiência e a qualidade do seu trabalho.'
    )