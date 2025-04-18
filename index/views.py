from index.utils import automation_tasks, schedule_smart, detail_report, equiip_control, first_view, and_now
from utils.utils import paginate
from blog.models import BlogPost
from utils.views import generic_view

# Create your views here.
def index(request):
    dados_paginados = paginate(
        request=request,
        data_objects=BlogPost.objects.filter(
            is_published=True
        ).order_by("-created_at"),
        per_page=5
    )

    contents = [
        {
            'type': 'card-no-tabs',
            'title_card': 'Bem vindo',
            'texts': first_view
        },
        {
            'type': 'card-left-tabs',
            'id': 1,
            'title_card': 'Funcionalidades',
            'tabs_title_contents': {
                'Automações de Tarefas': [automation_tasks],
                'Agendamento inteligente': [schedule_smart],
                'Relatorios detalhados': [detail_report],
                'Gestão de equipes': [equiip_control],
            }
        },
        {
            'type': 'card-no-tabs',
            'title_card': 'Escolhemos o zeladorX para operar nossa zeladoria, e agora?',
            'texts': and_now
        },
        {
            'type': 'posts-blog',
            'title_card': 'Blog e Conteúdos Recentes',
            'dados': dados_paginados
        },
    ]

    return generic_view(
        request=request,
        contents=contents,
        page_title='Eficiência e Controle na Gestão de Zeladoria.',
        page_name='Home',
        description='Simplifique operações e potencialize a produtividade com o ZeladorX.',
    )