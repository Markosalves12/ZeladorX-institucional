from django.contrib import admin
from .models import BlogPost, CategoriePost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')

class BlogCategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie',)
    list_filter = ('categorie', )

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(CategoriePost, BlogCategorieAdmin)