from django.shortcuts import render


# Create your views here.



# VISTA BASADA EN FUNCIÓN: página principal navbar
def pag_inicio(request):
    
    return render(request, "Bookrealm/index.html") # mostrar página




# VISTA BASADA EN FUNCIÓN: página principal navbar
def pag_about(request):
    return render(request, "Bookrealm/about.html") # mostrar página