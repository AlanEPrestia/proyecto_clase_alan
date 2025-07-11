from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Categoria
from ..forms import CategoriaForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'blog/categoria/list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'blog/categoria/form.html'
    success_url = reverse_lazy('categoria_list')