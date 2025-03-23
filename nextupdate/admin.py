from django.contrib import admin
from nextupdate.models import proximas_atualizacao

# Register your models here.
class NextUpdatesAdmin(admin.ModelAdmin):
    list_display = ('data', 'title', 'descricao', 'imagem', 'status', )
    list_display_links = ('data', 'title', 'descricao', 'imagem', 'status', )
    list_per_page = 20

admin.site.register(proximas_atualizacao, NextUpdatesAdmin)