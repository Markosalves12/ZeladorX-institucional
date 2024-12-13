from django.db import models
from django.utils import timezone

# Create your models here.
class proximas_atualizacao(models.Model):
    data = models.DateTimeField(
        default=timezone.now()
    )

    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    descricao = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
    )

    imagem = models.ImageField(
        upload_to="media/%Y/%m/%d/",
        blank=True,
    )

    status_options = [
        ('Planejado', 'Planejado'),
        ('Em Desenvolvimento', 'Em Desenvolvimento'),
        ('Em Testes', 'Em Testes'),
        ('Integrado ao sistema', 'Integrado ao sistema'),
    ]

    status = models.CharField(
        choices=status_options,
        max_length=30,
        blank=False,
        null=False,
        default='Planejado'
    )
