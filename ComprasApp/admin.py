from django.contrib import admin
from ComprasApp.models import Compra

# Register your models here.
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'libro', 'pago', 'fecha', 'id') # columnas a mostrar

    ordering = ('id', ) # ordenar por id (primero arriba, los últimos abajo)