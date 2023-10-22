from django import forms



class BuscarOferta(forms.Form):
    oferta = forms.CharField(required=True)