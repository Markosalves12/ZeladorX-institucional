from django.shortcuts import render

# Create your views here.
def generic_view(request, contents, page_title, page_name, description):
    return render(
        request=request,
        context={
            'page_title': page_title,
            'page_name': page_name,
            'description': description,
            'contents': contents
        },
        template_name='new_index.html'
    )