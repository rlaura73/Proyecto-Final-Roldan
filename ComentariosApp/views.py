# importación de librerías
from django.shortcuts import render, redirect # redireccionamiento
from django.urls import reverse_lazy # redireccionamiento para las vbc

from django.contrib.auth.decorators import login_required # decorador
from django.contrib.auth.mixins import LoginRequiredMixin # mixin

from django.views.generic import ListView # vbc
from django.views.generic.detail import DetailView # vbc
from django.views.generic.edit import CreateView, UpdateView, DeleteView # vbc

from UsuariosApp.models import Avatar # modelo
from ComentariosApp.models import Comentario # modelo
from ComentariosApp.forms import AgregarComentario # formularios
from datetime import datetime





# Create your views here.


# VISTA BASADA EN FUNCIÓN: página principal navbar --------------------------------------------------------
def pag_comentarios(request): # función Página Comentarios
    comentarios = Comentario.objects.all() # almacen de todos los comentarios
    avatares = Avatar.objects.all() # almacen de todos los comentarios

    mensaje = "" # mensaje a mostrar en caso de no haber ningun registro
    pasaje = {} # diccionario a pasar al archivo html

    if len(comentarios) > 0: # comprobar que hayan registros
        
        pasaje = {
            "comentarios":comentarios[::-1], # mostrar comentarios nuevos al principio
            "mensaje":mensaje, # mensaje vacío (hay registros)
            "avatares":avatares
        }
        return render(request, "Comentarios/comentarios.html", pasaje) # redirección
    else:
        mensaje = "No se encuentran registros por el momento..." # mensaje error (no hay registros)
        return render(request, "Comentarios/comentarios.html", {"mensaje":mensaje}) # redirección







# VISTA BASADA EN FUNCIÓN: para agregar un comentario, tienes que estar logueado ------------------------
@login_required # decorador
def agregar_comentario(request):

    mensaje = ""

    user = request.user # variable usuario

    if user.is_authenticated: # comprobar si ha iniciado sesion

        if request.method == "POST": # comprobar si envió datos

            form = AgregarComentario(request.POST) # variable formulario

            if form.is_valid(): # comprobar si el formulario es válido

                info = form.cleaned_data # se limpia la información

                # creamos nuevo registro a la base de datos (tabla Comentario)
                nvo_comentario = Comentario(
                    usuario = user, # campo usuario = variable usuario
                    encabezado = info["encabezado"], # campo encabezado = valor input encabezado
                    titulo = info["titulo"], # campo titulo = valor input titulo
                    comentario = info["comentario"], # campo comentario = valor input comentario
                )

                nvo_comentario.save() # guardamos el nuevo registro
                return redirect('PagComent')
        
        else:
            form = AgregarComentario()

        
        # diccionario a pasar al archivo formulario html
        pasaje = {
            "form":form,
            "mensaje":mensaje
        }

        return render(request, "Comentarios/agregarComent_form.html", pasaje)



# VISTA BASADA EN CLASE: SOLO PARA EL DUEÑO DEL COMENTARIO -----------------------------------------------
class EditarComentario(LoginRequiredMixin, UpdateView):
    model = Comentario
    template_name = "Comentarios/editarComent_form.html"
    success_url = reverse_lazy('PagComent')
    fields = ["encabezado", "titulo", "comentario"]


# VISTA BASADA EN CLASE: SOLO PARA EL DUEÑO DEL COMENTARIO -----------------------------------------------
class BorrarComentario(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = "Comentarios/coment_confirm_delete.html"
    success_url = reverse_lazy("PagComent")



# VISTA BASADA EN FUNCIÓN: SOLO PARA EL USUARIO LOGUEADO --------------------------------------------------
@login_required # decorador
def mis_comentarios(request): # función

    var_usuario = request.user # variable para comprobar que se ha logueado el usuario

    comments = Comentario.objects.filter(usuario = request.user.id) # variable para traer todos los comentarios exclusivamente del usuario logueado
    avatares = Avatar.objects.all() # para desplegar el avatar en el comentario

    if var_usuario.is_authenticated:

        mensaje = "" # variable a mostrar en caso que no se encuentren registros

        if len(comments) > 0: # comprobar que haya registros

            # envío de datos para el html
            pasaje = {
                "comentarios":comments,
                "avatares":avatares,
                "mensaje":mensaje
            }

            return render(request, "Comentarios/mis_comentarios.html", pasaje) # url en caso que se hayan encontrado registros
        
        else:
            mensaje = "Registros inexistentes." # mensaje error: no se han encontrado registros
            return render(request, "Comentarios/mis_comentarios.html", {"mensaje":mensaje}) # url + mensaje