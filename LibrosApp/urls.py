from django.urls import path
from LibrosApp import views
from django.views.generic import TemplateView
from django.views.defaults import permission_denied

urlpatterns = [
    path('', views.pag_libros, name="PagLibros"), # página principal
    path('nuevo-libro/', views.AgregarLibroCV.as_view(), name="AgregarLibro"),
    path('detalle-libro/<int:pk>/', views.DetalleLibroDv.as_view(), name="DetalleLibro"),
    path('modificar-libro/<int:pk>/', views.editar_libro, name="EditarLibro"),
    path('eliminar-libro/<int:pk>/', views.EliminarLibroDV.as_view(), name="EliminarLibro"),
    path('busqueda-libro/', views.buscar_libros, name="BuscarLibros"),

    path('403/', views.permisos_negados, name="PermisosNegados") # en caso de saltar algun error
]