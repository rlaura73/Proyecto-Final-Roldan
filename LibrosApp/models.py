from django.db import models
from django.conf import settings

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.CharField(max_length=10)
    oferta = models.CharField(max_length=5)

    def __str__(self):  # renombrar objetos
        return f"{self.titulo}"
    



class Portada(models.Model):
    book = models.OneToOneField(Libro, on_delete=models.CASCADE, null=True, blank=True) # qué libro
    portada = models.ImageField(upload_to='portadas', null=True, blank=True) # incluir imagen
    previa_img1 = models.ImageField(upload_to='previas', null=True, blank=True) # lectura disponible
    previa_img2 = models.ImageField(upload_to='previas', null=True, blank=True) # lectura disponible

    def __str__(self):
        return f"{settings.MEDIA_URL}{self.portada}"