from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from ..models import Entrada
from ..forms import EntradaForm

class EntradaListView(ListView):
    model = Entrada
    template_name = 'blog/entrada/list.html'
    context_object_name = 'entradas'
    ordering = ['-fecha_creacion']

class EntradaDetailView(DetailView):
    model = Entrada
    template_name = 'blog/entrada/detail.html'
    context_object_name = 'entrada'

class EntradaCreateView(LoginRequiredMixin, CreateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog/entrada/form.html'
    success_url = reverse_lazy('entrada_list')

class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog/entrada/form.html'
    success_url = reverse_lazy('entrada_list')

class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    model = Entrada
    template_name = 'blog/entrada/confirm_delete.html'
    success_url = reverse_lazy('entrada_list')