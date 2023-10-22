from django.urls import path
from ComprasApp import views

urlpatterns = [
    path('mis-compras/', views.listar_compras, name="PagCompras"), # página principal
    path('comprar-libro/<int:pk>/', views.comprar_libro, name="Comprar"),
    path('detalle-compra/<int:pk>/', views.detalle_compra, name="DetalleCompra")
]