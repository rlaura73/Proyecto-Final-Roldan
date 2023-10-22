from django.contrib import admin
from UsuariosApp.models import Avatar

# Register your models here.
@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("user", "avatar") # columnas a mostrar

    ordering = ("id", ) # ordenar por id (primero arriba, los últimos abajo)