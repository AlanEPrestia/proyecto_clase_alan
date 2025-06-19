from django import forms
from .models import Autor, Categoria, Entrada

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 6}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
