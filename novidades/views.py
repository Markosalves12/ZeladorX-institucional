from novidades.utils import new_macro
from utils.views import generic_view

# Create your views here.
def equipamentos_e_manutencao(request):
    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Novo Macro serviço em desenvolvimento',
            'texts': new_macro
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Eficiência e Controle na Gestão de Zeladoria.',
        page_name='Novidades',
        description='Simplifique operações e potencialize a produtividade com o ZeladorX.',
    )