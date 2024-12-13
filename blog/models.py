from django.db import models

# Create your models here.
class CategoriePost(models.Model):
    categorie = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        return self.categorie

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    categorie_post = models.ManyToManyField(
        to=CategoriePost,
        null=False,
        blank=False,
        related_name='categoriepost'
    )
    foto = models.ImageField(
        upload_to="media/%Y/%m/%d/",
        blank=True,
    )

    def __str__(self):
        return self.title