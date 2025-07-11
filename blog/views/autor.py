from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ..models import Autor
from ..forms import AutorForm


class AutorListView(ListView):
    model = Autor
    template_name = 'blog/autor/list.html'
    context_object_name = 'autores'

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'blog/autor/form.html'
    success_url = reverse_lazy('autor_list')