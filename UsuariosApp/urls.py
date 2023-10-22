from django.urls import path
from django.contrib.auth.views import LogoutView
from UsuariosApp import views


urlpatterns = [
    path('inicio-sesion/', views.login_request, name="Login"),
    path('registro/', views.registrar_usuario, name="Registro"), 
    path('perfil/', views.pag_usuario, name="PagUsuario"),
    path('logout/', LogoutView.as_view(template_name = "Bookrealm/index.html"), name="Logout"),
    path('editar/', views.editar_perfil, name="EditarPerfil"),
]
