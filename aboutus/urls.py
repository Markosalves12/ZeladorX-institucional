from django.urls import path
from aboutus.views import missao, visao, valores

urlpatterns = [
    path('sobre-nos/missao', missao, name='missao'),
    path('sobre-nos/visao', visao, name='visao'),
    path('sobre-nos/valores', valores, name='valores'),
]