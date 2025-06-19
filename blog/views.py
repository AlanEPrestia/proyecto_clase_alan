from django.shortcuts import render,redirect

from .forms import EntradaForm
from .models import Entrada

def inicio(request):
    entradas = Entrada.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/index.html', {'entradas': entradas})

def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_entrada')  # o a una página de confirmación
    else:
        form = EntradaForm()
    return render(request, 'blog/entrada_form.html', {'form': form})

def buscar_entrada(request):
    query = request.GET.get('query')
    resultados = Entrada.objects.filter(titulo__icontains=query) if query else []
    return render(request, 'blog/buscar.html', {'resultados': resultados})
