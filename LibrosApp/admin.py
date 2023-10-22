from django.contrib import admin
from LibrosApp.models import *

# Register your models here.
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "stock", "precio", "oferta", "autor", "editorial") # columnas a mostrar

    ordering = ("id", ) # ordenar por id (primero arriba, los últimos abajo)
    search_fields = ("oferta", "editorial") # mostrar barra de búsqueda



@admin.register(Portada)
class PortadaAdmin(admin.ModelAdmin):
    list_display = ("book", "portada") # columnas a mostrar

    ordering = ("id", ) # ordenar por id (primero arriba, los últimos abajo)