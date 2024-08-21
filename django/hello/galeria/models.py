from django.db import models

# Create your models here.

class Fotografia(models.Model):
    nome = models.CharField(
        max_length=100,
        null=False
    )
    legenda = models.CharField(
        max_length=150,
        null=False
    )
    descricao = models.TextField(
        null=False
    )
    foto = models.CharField(
        max_length=100,
        null=False
    )