from django.contrib import admin
from ComentariosApp.models import Comentario

# Register your models here.

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("usuario", "comentario", "fecha") # columnas a mostrar

    ordering = ("id", ) # ordenar por id (primero arriba, los últimos abajo)