from django.shortcuts import render
from nextupdate.models import proximas_atualizacao
from utils.utils import paginate

# Create your views here.
def atualizacoes(request):
    dados_paginados = paginate(
        request=request,
        data_objects=proximas_atualizacao.objects.all().order_by('-data'),
        per_page=5
    )

    contents = [
        {
            'type': 'models-by-jungle',
            'title_card': 'Missão',
            'dados': dados_paginados
        }
    ]

    return render(
        request=request,
        context={
            'page_title': 'Atualizações',
            'page_name': 'Novidades e Melhorias Futuras',
            'description': 'Descubra as inovações que estão por vir no ZeladorX. Estamos comprometidos em trazer novas '
                           'funcionalidades que transformam a gestão de zeladoria.',
            'contents': contents,
        },
        template_name='new_index.html'
    )