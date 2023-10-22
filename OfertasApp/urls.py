from django.urls import path
from OfertasApp import views

urlpatterns = [
    path('', views.pag_ofertas, name="PagOfertas"), # página principal navbar
    path('busqueda-oferta/', views.buscar_ofertas, name="BuscarOferta")
]