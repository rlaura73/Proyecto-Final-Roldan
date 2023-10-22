from django import forms



class BuscarLibro(forms.Form):
    titulo = forms.CharField()




class NuevoLibro(forms.Form):
    titulo = forms.CharField(required=True)
    autor = forms.CharField(required=True)
    editorial = forms.CharField(required=True)
    stock = forms.IntegerField(required=True)
    precio = forms.CharField(required=True)
    oferta = forms.CharField(required=True)





class EditarLibro(forms.Form):
    titulo = forms.CharField(required=False)
    autor = forms.CharField(required=False)
    editorial = forms.CharField(required=False)
    stock = forms.IntegerField(required=False)
    precio = forms.CharField(required=False)
    oferta = forms.CharField(required=False)

    portada = forms.ImageField(label="Portada", required=True) # cargar imagen
    previa1 = forms.ImageField(label="Previa 1", required=True) # cargar imagen
    previa2 = forms.ImageField(label="Previa 2", required=True) # cargar imagen