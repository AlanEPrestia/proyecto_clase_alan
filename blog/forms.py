from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Entrada, Autor, Categoria
from django.contrib.auth.models import User
from blog.models import Avatar


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'biografia']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User  # Indica con que modelo guiarse
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="Ingrese su email:")
    # password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label="Nombre de usuario")

    last_name = forms.CharField()
    first_name = forms.CharField()
    is_active = forms.BooleanField(required=False, label="¿Está activo?")

    class Meta:
        model = User
        # fields = ('email', 'password')
        fields = ('username', 'email', 'last_name', 'first_name', 'is_active')

class AvatarForm(forms.ModelForm):
    
    class Meta:
        model = Avatar
        fields = ['imagen']