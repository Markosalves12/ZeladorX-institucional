from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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