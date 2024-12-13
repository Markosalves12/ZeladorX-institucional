from django.shortcuts import render
from .models import BlogPost
from utils.utils import paginate

def blog_home(request):
    dados_paginados = paginate(
        request=request,
        data_objects=BlogPost.objects.filter(
            is_published=True
        ).order_by("-created_at"),
        per_page=5
    )

    contents = [
        {
            'type': 'blog',
            'title_card': 'Blog e Conteúdos Recentes',
            'dados': dados_paginados
        },
    ]

    return render(
        request=request,
        context={
            'page_title': 'Blog',
            'page_name': 'Blog',
            'desciption': 'Simplifique operações e potencialize a produtividade com o ZeladorX.',
            'contents': contents
        },
        template_name='new_index.html'
    )