from django.urls import path
from nextupdate.views import atualizacoes
urlpatterns = [
    path('proximas-atualizacoes/', atualizacoes, name='atualizacoes'),
]