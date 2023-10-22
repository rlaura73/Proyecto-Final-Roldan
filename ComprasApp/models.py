# importacion de librerias
from django.db import models
from django.contrib.auth.models import User

from LibrosApp.models import Libro

from datetime import datetime

# Create your models here.

timezone = datetime.now()

class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # quien realiza la compra
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE) # qué compra
    precio = models.CharField(max_length=10, null=True, blank=True) # precio final
    oferta = models.CharField(max_length=5, null=True, blank=True) # mostar si hubo o no ofertar al momento de la compra
    pago = models.CharField(max_length=50) # con qué paga
    fecha = models.DateTimeField(default=timezone.now) # cuándo se realizó la compra

    def __str__(self): # renombrar objetos
        return f"{self.usuario} - {self.libro}"
    

# ningun campo acepta nulos