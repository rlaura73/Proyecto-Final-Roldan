# importación de librerías
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from LibrosApp.models import *
from OfertasApp.forms import *
from UsuariosApp.models import *
from datetime import datetime

# Create your views here.


# VISTA BASADA EN FUNCIÓN: mostrar todas las ofertas
def pag_ofertas(request): # pagina principal navbar
    libros = Libro.objects.all() # encontrar registros de libros
    portadas = Portada.objects.all() # encontrar portadas de los mismos
    
    mensaje = "" # mensaje en caso de no haber registros

    if len(libros) > 0: # comprobar que haya registros
        mensaje = "" # mensaje vacío
    else:
        mensaje = "No se encuentran registros en el sistema." # mensaje error
    

    # diccionario a pasar al archivo html
    pasaje = {
        "libros":libros,
        "portadas":portadas,
        "mensaje":mensaje
    }


    return render(request, "Ofertas/ofertas.html", pasaje) # mostrar página






# VISTA BASADA EN FUNCIÓN: búsqueda de ofertas disponibles
def buscar_ofertas(request):
    if request.method == "POST": # comprobar envío de datos

        form = BuscarOferta(request.POST) # uso de formulario

        if form.is_valid(): # comprobar si el formulario es válido

            info = form.cleaned_data # limpiar datos

            libros = Libro.objects.filter(oferta__icontains=info["oferta"]) # filtrar de acuerdo a los datos enviados

            portadas = Portada.objects.all()

            pasaje_variables = {
                "libros":libros,
                "portadas":portadas
            }

            return render(request, "Ofertas/result_busq_ofertas.html", pasaje_variables) # mostrar página
        
        else:
            print("formulario invalido")
    
    else:
        form = BuscarOferta()

    
    return render(request, "Ofertas/busq_ofertas.html") # mostrar página formulario