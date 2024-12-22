from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import EmailMessage, send_mail
from setup.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def paginate(request, data_objects, per_page=10):
    paginator = Paginator(data_objects, per_page=per_page)
    page_number = request.GET.get('page')

    try:
        elementos_paginados = paginator.page(page_number)
    except PageNotAnInteger:
        # Se o número da página não for um número inteiro, retorne a primeira página
        elementos_paginados = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (por exemplo, 9999), retorne a última página de resultados
        elementos_paginados = paginator.page(paginator.num_pages)

    return elementos_paginados

def enviar_notificacao(destinatario, assunto, contexto, template):
    html_content = render_to_string(
        template_name=template,
        context=contexto
    )
    text_contex = strip_tags(html_content)

    send_mail(
        assunto,
        text_contex,
        EMAIL_HOST_USER,
        destinatario,
        html_message=html_content,
    )