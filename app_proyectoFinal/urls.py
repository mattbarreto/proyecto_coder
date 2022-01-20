from django.urls import path
from app_proyectoFinal.views import buscar, inicio, atleta, entrenador, rutina, atletas_form, busqueda_atletas

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('atletas', atleta, name='Atletas'),
    path('entrenadores', entrenador, name='Entrenadores'),
    path('rutina', rutina, name='Rutinas'),
    path('atletas_form', atletas_form, name='Formulario de Atletas'),
    path('buscarAtletas', busqueda_atletas, name='Busqueda atletas'),
    path('buscar', buscar, name='Buscar'),
]