from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('entrada/nueva/', views.crear_entrada, name='crear_entrada'),
    path('entrada/buscar/', views.buscar_entrada, name='buscar_entrada'),
]
