from django.urls import path
from app_proyectoFinal.views import inicio, atleta, entrenador, rutina

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('atletas', atleta, name='Atletas'),
    path('entrenadores', entrenador, name='Entrenadores'),
    path('rutina', rutina, name='Rutinas'),
]
