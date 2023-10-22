from django.shortcuts import render

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from UsuariosApp.forms import IniciarSesion, RegistroUsuario, EditarPerfil
from UsuariosApp.models import Avatar



# Create your views here.



# VISTA BASADA EN FUNCIÓN: página perfil de usuario --------------------------------------------------------
@login_required # decorardor
def pag_usuario(request):
    usuario = request.user

    if usuario.is_authenticated: # comprobar que el usuario haya iniciado sesión
        return render(request, "Usuarios/usuario.html") # mostrar página
    else:
        return render(request, "Bookrealm/index.html") # mostrar página




# VISTA BASADA EN FUNCIÓN: para loguearse ------------------------------------------------------------------
def login_request(request):

    if request.user.is_authenticated:
        return render(request, "Bookrealm/index.html")

    else:
        if request.method == "POST": # comprobar envío de datos

            form = IniciarSesion(request, data = request.POST) # uso de formulario

            if form.is_valid(): # comprobar si el formulario es válido
                usuario = form.cleaned_data.get("username")
                clave = form.cleaned_data.get("password")

                user = authenticate(username = usuario, password = clave)

                if usuario is not None:
                    login(request, user)

                    return render(request, "Bookrealm/index.html") # mostrar página
                
            else:
                return render(request, "Usuarios/login.html", {"mensaje":"Error, datos incorrectos"})


        form = IniciarSesion()

        return render(request, "Usuarios/login.html", {"form":form}) # mostrar página






# VISTA BASADA EN FUNCIÓN: para registrarse --------------------------------------------------------------
def registrar_usuario(request):

    if request.user.is_authenticated:

        return render(request, "Bookrealm/index.html")
    
    else:
        if request.method == "POST": # comprobar envío de datos

            form = RegistroUsuario(request.POST) # uso de formulario

            if form.is_valid(): # comprobar si el formulario es válido

                username = form.cleaned_data["username"]
                form.save()

                return render(request, "Bookrealm/index.html") # mostrar página

        else:
            # form = UserCreationForm()
            form = RegistroUsuario()

        return render(request, "Usuarios/registro.html", {"form":form}) # mostrar página




# VISTA BASADA EN FUNCIÓN: para editar perfil ------------------------------------------------------------
@login_required # decorardor
def editar_perfil(request):
    usuario = request.user

    if usuario.is_authenticated: # comprobar si el usuario inició sesión

        if request.method == "POST": # comprobar envío de datos
            form = EditarPerfil(request.POST, request.FILES) # uso de formulario

            if form.is_valid(): # comprobar si el formulario es válido
                info = form.cleaned_data # limpiar datos

                if info["password1"] != info["password2"]: # comprobar que las contraseñas sean iguales

                    # diccionario a pasar al formulario
                    datos = {
                        "first_name":usuario.first_name,
                        "email":usuario.email
                    }

                    form = EditarPerfil(initial=datos) # plasmar diccionario

                else:

                    # registrar cambios
                    usuario.email = info["email"]
                    usuario.first_name = info["first_name"]
                    usuario.last_name = info["last_name"]
                    if info["password1"]:
                        usuario.set_password(info["password1"])
                    usuario.save() # guardar cambios


                    # agregar imagen (avatar)
                    try:
                        avatar = Avatar.objects.get(user=usuario)
                    except Avatar.DoesNotExist:
                        avatar = Avatar(user=usuario, avatar=info["avatar"])
                        avatar.save()
                    else:
                        avatar.imagen = info["avatar"]
                        avatar.save()


                    return render(request, "Usuarios/usuario.html") # mostrar página
                
            else:
                print("formulario invalido")
        
        else:

            # diccionario a pasar al formulario
            datos = {
                "email":usuario.email,
                "first_name":usuario.first_name,
                "last_name":usuario.last_name,
            }

            form = EditarPerfil(initial=datos) # plasmar diccionario

        
        return render(request, "Usuarios/editarPerfil_form.html", {"form":form}) # mostrar página
    
    else:
        return render(request, "Bookrealm/index.html", {"mensaje":"Error, no puedes acceder a esta página"}) # mostrar página