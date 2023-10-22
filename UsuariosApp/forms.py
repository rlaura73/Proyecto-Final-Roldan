# importación librerías
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



# formulario para iniciar sesión
class IniciarSesion(AuthenticationForm):
    username = forms.CharField(label="Usuario", widget=forms.TextInput)
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)



# formulario para registrarse en el sistema
class RegistroUsuario(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField(label="Correo")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        help_texts = {k:"" for k in fields}




# formulario para editar perfil
class EditarPerfil(UserCreationForm):

    email = forms.EmailField(label="Correo", required=False)
    first_name = forms.CharField(label="Nombre", required=False)
    last_name = forms.CharField(label="Apellido", required=False)
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput, required=False)

    avatar = forms.ImageField(label="Subir avatar", required=False)


    class Meta:
        model = User
        fields = ['email','first_name', 'last_name', 'password1', 'password2']

        help_texts = {k:"" for k in fields}