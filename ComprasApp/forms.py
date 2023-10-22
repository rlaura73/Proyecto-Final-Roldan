from django import forms


class ComprarLibro(forms.Form):
    pago = forms.CharField(label="Metodo de pago", required=True, max_length=50)