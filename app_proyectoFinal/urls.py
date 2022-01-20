from django.urls import path
from app_proyectoFinal.views import atleta_busqueda, buscar, inicio, atleta, entrenador, rutina, atletas_form

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('atletas', atleta, name='Atletas'),
    path('entrenadores', entrenador, name='Entrenadores'),
    path('rutina', rutina, name='Rutinas'),
    path('atletas_form', atletas_form, name='Formulario de Atletas'),
    path('buscarAtleta', atleta_busqueda, name='Busqueda de Atletas'),
    path('buscar', buscar, name='Buscar'),
]