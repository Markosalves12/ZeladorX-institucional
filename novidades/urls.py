from django.urls import path
from novidades.views import equipamentos_e_manutencao

urlpatterns = [
    path('equipamentos-e-manutencao', equipamentos_e_manutencao, name='equipamentos_e_manutencao'),
]