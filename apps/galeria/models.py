from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
import os

def upload_to_fotos(instance, filename):
    ext = os.path.splitext(filename)[1]
    nome_aleatorio = uuid.uuid4().hex
    return f"fotos/{nome_aleatorio}{ext}"

class Fotografia(models.Model):

    OPECOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALAXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPECOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to=upload_to_fotos, blank=False, null=False)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user")

    def __str__(self):
        return f"Fotografia [nome={self.nome}, legenda={self.legenda}, descricao={self.descricao}, foto={self.foto}]"
