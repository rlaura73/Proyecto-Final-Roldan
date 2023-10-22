from django import forms



class AgregarComentario(forms.Form):
    encabezado = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Ej: 1/5, 4/5, etc'})) # titulo principal
    titulo = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Titulo principal'})) # titulo secundario
    comentario = forms.CharField(widget=forms.Textarea, required=True) # cuerpo mensaje

# se usan estos 3 campos debido a que los otros se cargan de forma interna