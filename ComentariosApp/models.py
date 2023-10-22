from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.

timezone = datetime.now()

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # persona que agrega el comentario
    encabezado = models.CharField(max_length=200) # titulo principal
    titulo = models.CharField(max_length=200) # titulo secundario
    comentario = models.CharField(max_length=500) # cuerpo mensaje
    fecha = models.DateTimeField(default=timezone.now) # fecha subida del comentario

    def __str__(self):  # renombrar objetos
        return f"{self.usuario} - {self.encabezado} - {self.fecha}"

# ningun campo acepta nulos