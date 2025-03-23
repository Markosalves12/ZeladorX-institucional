from django.urls import path
from suporte.views import FAQ, contato
from suporte.views_jardinagem import manual_jardinagem, tutoriais_jardinagem
from suporte.views_limpeza_predial import manual_limpeza_predial, tutoriais_limpeza_predial

urlpatterns = [
    path('suporte/manual-jardinagem', manual_jardinagem, name='manual_jardinagem'),
    path('suporte/manual-limpeza-predial', manual_limpeza_predial, name='manual_limpeza_predial'),
    path('suporte/FAQ', FAQ, name='FAQ'),
    path('suporte/contato', contato, name='contato'),
    path('suporte/tutoriais-jardinagem', tutoriais_jardinagem, name='tutoriais_jardinagem'),
    path('suporte/tutoriais-limpeza-predial', tutoriais_limpeza_predial, name='tutoriais_limpeza_predial'),
]