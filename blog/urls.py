from django.urls import path
from blog.views.entrada import (
    EntradaListView, EntradaDetailView, EntradaCreateView,
    EntradaUpdateView, EntradaDeleteView)
from blog.views.autor import (AutorListView, AutorCreateView)
from blog.views.categoria import (CategoriaListView, CategoriaCreateView)    
from django.views.generic import TemplateView
from blog.views.usuario import login_request, register, editarPerfil, upload_avatar
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', EntradaListView.as_view(), name='entrada_list'),
    path('entrada/<int:pk>/', EntradaDetailView.as_view(), name='entrada_detail'),
    path('entrada/nueva/', EntradaCreateView.as_view(), name='entrada_create'),
    path('entrada/<int:pk>/editar/', EntradaUpdateView.as_view(), name='entrada_update'),
    path('entrada/<int:pk>/borrar/', EntradaDeleteView.as_view(), name='entrada_delete'),
    path('autores/', AutorListView.as_view(), name='autor_list'),
    path('autores/nuevo/', AutorCreateView.as_view(), name='autor_create'),
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nueva/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('about/', TemplateView.as_view(template_name='blog/about.html'), name='about'),

    path('login/', login_request, name='login'),
    path('registro/', register, name='registro'),
    path('logout', LogoutView.as_view(template_name='blog/usuarios/logout.html'), name='logout'),

    path('editar-perfil/', editarPerfil, name='editarPerfil'),
    path('avatar/', upload_avatar, name='upload_avatar'),
]