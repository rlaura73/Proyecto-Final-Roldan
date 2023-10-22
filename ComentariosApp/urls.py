from django.urls import path
from ComentariosApp import views

urlpatterns = [
    path('', views.pag_comentarios, name="PagComent"), # página principal
    path('agregar-comentario/', views.agregar_comentario, name="AgregarComentario"),
    path('editar-comentario/<int:pk>/', views.EditarComentario.as_view(), name="EditarComent"),
    path('eliminar-comentario/<int:pk>/', views.BorrarComentario.as_view(), name="EliminarComent"),
    path('mis-comentarios/', views.mis_comentarios, name="MisComent")
]