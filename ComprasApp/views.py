# importacion de librerias
from django.shortcuts import render
from django.urls import reverse_lazy

# VBC
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required # decorador
from django.contrib.auth.mixins import LoginRequiredMixin # mixin
from django.contrib.auth.context_processors import auth


from ComprasApp.models import *
from ComprasApp.forms import *
from LibrosApp.models import *
from UsuariosApp.models import *
from datetime import datetime


# Create your views here.


# VISTA BASADA EN FUNCIÓN: para que el usuario vea todas las compras que realizó ----------------------------
@login_required # decorador
def listar_compras(request):
    var_usuario = request.user
    mensaje = ""

    if var_usuario.is_authenticated: # comprobar que esté el usuario logueado
        compras = Compra.objects.filter(usuario=request.user.id) # encontrar todos los registros del usuario
        libros = Libro.objects.all() # almacenar todos los registros de libros

        if len(compras) > 0:
            mensaje = ""
        else:
            mensaje = "No hay registros por el momento..."

        # diccionario a pasar al archivo html
        pasaje = {
            "compras":compras[::-1],
            "libros":libros,
            "mensaje":mensaje
        }

        return render(request, 'Compras/compras.html', pasaje) # mostrar página





# VISTA BASADA EN CLASE: ver detalle de la compra
@login_required
def detalle_compra(request, pk):

    compra = Compra.objects.get(id = pk)
    libros = Libro.objects.all()

    var_usuario = request.user

    if var_usuario.is_authenticated:

        pasaje_variables = {
            "compra":compra,
            "libros":libros
        }

        return render(request, "Compras/compra_detalle.html", pasaje_variables)







# VISTA BASADA EN FUNCIÓN: para que sea el usuario quien realice la compra ---------------------------------
@login_required # decorador
def comprar_libro(request, pk): # necesitamos de un id para encontrar el libro a comprar


    # para registrar el momento de la compra
    dt = datetime.now()

    y = dt.year
    mth = dt.month
    d = dt.day
    h = dt.hour
    mn = dt.minute
    s = dt.second

    ahora = str(y) + "-" + str(mth) + "-" + str(d) + " " + str(h) + ":" + str(mn) + ":" + str(s)
    d = dt.strftime("%d/%B/%Y, %H:%M:%S")
    # ..........................................


    book = Libro.objects.get(id = int(pk)) # encontrar el libro con el id

    precio_final = float(book.precio) # variable total a pagar, conversión string a float

    var_oferta = ""

    # función interna: calcular la oferta
    def calculo_porcentaje(precio, porcentaje):
        monto = float(porcentaje) / 100
        cant_a_restar = precio * monto
        return cant_a_restar

    
    if book.oferta != "0%": # comprobar que haya oferta
        var_oferta = book.oferta # almacenar oferta del libro
        var_oferta = var_oferta.split("%")[0] # retiramos simbolo porcentaje, en caso de haber

        precio_final -= calculo_porcentaje(precio_final, var_oferta) # restamos del total a pagar


    precio_final = str(precio_final) # conversión float a string


    var_usuario = request.user
    mensaje = ""

    if var_usuario.is_authenticated: # comprobar que haya un usuario logueado

        if request.method == "POST": # comprobar que se envió datos

            form = ComprarLibro(request.POST) # uso de formulario

            if form.is_valid(): # comprobar que el formulario sea válido

                if book.stock > 0: # comprobar que haya stock disponible
                    
                    info = form.cleaned_data # limpiar datos
                    
                    # nuevo registro en la base de datos (tabla Compra)
                    compra = Compra(
                        usuario = var_usuario, # pasar el usuario logueado
                        libro = book, # pasar el libro a comprar
                        precio = precio_final, # pasar el precio final
                        oferta = book.oferta, # pasar si hubo oferta del libro
                        pago = info["pago"], # pasar el método de pago
                    )

                    compra.save() # guardar registro

                    book.stock -= 1 # actualizar stock del libro
                    book.save() # guardar cambios

                    mensaje = f"Se ha enviado el vínculo de pago al correo {var_usuario.email}"
                    pasaje = {
                        "mensaje":mensaje
                    }

                    return render(request, "Usuarios/usuario.html", pasaje) # mostrar página
                

                else:
                    mensaje = "no hay stock disponible :("
                    return render(request, "Usuarios/usuario.html", {"mensaje":mensaje})
                
                
            
            else:
                mensaje = "Error, algo sucedió"
                return render(request, "Usuarios/usuario.html", {"mensaje":mensaje})

        else:
            form = ComprarLibro()

        
        # diccionario a pasar al archivo html
        pasaje_final = {
            "form":form,
            "pk":pk,
            "libro":book,
            "now":d,
            "total":precio_final
        }
        
        return render(request, "Compras/comprar_form.html", pasaje_final) # mostar página