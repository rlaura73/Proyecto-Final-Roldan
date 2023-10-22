# importación de librerias
from typing import Any
from django.shortcuts import render, redirect # mostrar páginas
from django.urls import reverse_lazy # mostrar página designando url

# vbc
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.defaults import permission_denied

from django.contrib.auth.decorators import login_required # decorador
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # mixin

from django.contrib.auth.context_processors import auth


from LibrosApp.models import *
from LibrosApp.forms import *
from UsuariosApp.models import *
from datetime import datetime



# Create your views here.



# VISTA BASADA EN FUNCIÓN: página principal navbar -------------------------------------------------------
def pag_libros(request):
    libros = Libro.objects.all() # almacenar registros de libros
    portadas = Portada.objects.all() # almacenar registros de portadas de los mismos
    
    mensaje = "" # mensaje en caso de no haber registros

    if len(libros) > 0: # comprobar que haya registros
        mensaje = "" # mensaje vacío
    else:
        mensaje = "No se encuentran registros en el sistema." # mensaje error
    

    # diccionario a pasar al archivo html
    pasaje = {
        "libros":libros[::-1],
        "portadas":portadas,
        "mensaje":mensaje
    }


    return render(request, "Libros/libros.html", pasaje) # mostrar página




# VISTA BASADA EN FUNCIÓN: búsqueda de libros por título --------------------------------------------------
def buscar_libros(request):

    mensaje = ""
    
    if request.method == "POST": # comprobar envío de datos

        form = BuscarLibro(request.POST) # uso de formulario

        if form.is_valid(): # comprobar si el formulario es válido

            info = form.cleaned_data # limpiar los datos

            libros = Libro.objects.filter(titulo__icontains=info["titulo"]) # filtrar registros de acuerdo al dato ingresado

            imagenes = Portada.objects.all() # necesario si el libro tiene portada o no

            pasaje_variables = {
                "imagenes":imagenes,
                "libros":libros,
                "mensaje":mensaje
            }

            if len(libros) > 0:

                mensaje = ""

                return render(request, "Libros/result_busq_libros.html", pasaje_variables) # mostrar página
            
            else:
                mensaje = "No hay resultados"
                return render(request, "Libros/result_busq_libros.html", {"mensaje":mensaje})
        
        else:
            print("formulario invalido")
    
    else:
        form = BuscarLibro()

    
    return render(request, "Libros/busq_libros.html") # mostrar página formulario








# VISTA BASADA EN CLASE: mostrar detalle del libro ---------------------------------------------------------
class DetalleLibroDv(DetailView):
    model = Libro
    template_name = "Libros/libro_detalle.html"
    context_object_name = "libro"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Libro.DoesNotExist:
            return redirect('PagInicio')  # Si el libro no existe, devuelve None

    def get(self, request, *args, **kwargs):
        try:
            libro_actual = self.get_object()
            if libro_actual is not None:
                if libro_actual.stock > 0:
                    return super().get(request, *args, **kwargs)  # Continuar a la vista de detalle
                else:
                    return redirect('PagInicio')  # Redirigir a otra página
            else:
                return redirect('PagInicio')
        except:
            return render(request, 'Bookrealm/index.html')
        



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        libro_actual = self.get_object()  # Obten el libro actual
        try:
            context['portada'] = Portada.objects.get(book=libro_actual)
        except Portada.DoesNotExist:
            context['portada'] = ""
        
        context['l'] = "Harry Potter y las Reliquias de la Muerte"

        return context




# VISTA BASADA EN CLASE: agregar libro (exclusivo admin / staff) -------------------------------------------
class AgregarLibroCV(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = Libro
    permission_required = ("Libro.add_post")
    template_name = "Libros/agregarLibro_form.html"
    success_url = reverse_lazy("PagLibros")
    fields = ["titulo", "autor", "editorial", "stock", "precio", "oferta"]

    def test_func(self):
        return superusuario_staff(self.request.user)
    
    def handle_no_permission(self):
        return redirect('PagInicio')

# función para la vista basada en clase: agregar libro
def superusuario_staff(user):
    return user.is_superuser or user.is_staff

# función para mostrar la página inicio en caso de error
def permisos_negados(request, exception):
    return TemplateView.as_view(template_name="Bookrealm/index.html")(request)


# VISTA BASADA EN CLASE: eliminar libro (exclusivo admin / staff) -------------------------------------------
class EliminarLibroDV(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Libro
    template_name = "Libros/libro_confirm_delete.html"
    success_url = reverse_lazy("PagLibros")

    def test_func(self):
        return superusuario_staff(self.request.user)
    
    def handle_no_permission(self):
        return redirect('PagInicio')






# VISTA BASADA EN FUNCIÓN: editar libro (exclusivo admin / staff) ------------------------------------------
@login_required
def editar_libro(request, pk):
    usuario = request.user
    try:
        libro = Libro.objects.get(id = pk) # encontrar el libro con el id
    except:
        pass

    if usuario.is_superuser or usuario.is_staff: # comprobar que el usuario sea admin / staff

        if request.method == "POST": # comprobar envío de datos

            form = EditarLibro(request.POST, request.FILES) # uso de formulario

            if form.is_valid(): # comprobar si el formulario es válido

                info = form.cleaned_data # limpiar los datos

                # edición del registro
                libro.titulo = info["titulo"]
                libro.autor = info["autor"]
                libro.editorial = info["editorial"]
                libro.stock = info["stock"]
                libro.precio = info["precio"]
                libro.oferta = info["oferta"]

                libro.save() # guardar cambios del registro

                # nuevo registro de imagen del libro
                try:
                    port = Portada.objects.get(book=libro)
                except Portada.DoesNotExist:
                    port = Portada(
                        book=libro,
                        portada=info["portada"],
                        previa_img1 = info["previa1"],
                        previa_img2 = info["previa2"]
                        )
                    port.save()
                else:
                    port.portada = info["portada"]
                    port.previa_img1 = info["previa1"]
                    port.previa_img2 = info["previa2"]
                    port.save()
                

                return redirect('PagLibros') # mostrar página
            
            else:
                print("formulario invalido")
        
        else:

            # diccionario a pasar al archivo html
            datos = {
                "titulo":libro.titulo,
                "autor":libro.autor,
                "editorial":libro.editorial,
                "stock":libro.stock,
                "precio":libro.precio,
                "oferta":libro.oferta
            }

            form = EditarLibro(initial=datos) # mostrar los datos previamente cargados

        
        return render(request, "Libros/editarLibro_form.html", {"form":form}) # mostrar página
    
    else:
        return render(request, "Bookrealm/index.html")