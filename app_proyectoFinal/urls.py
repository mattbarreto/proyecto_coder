from django.urls import path
from app_proyectoFinal.views import atleta_alta, buscar, inicio, atleta, atleta_alta, atleta_delete, atleta_update ,atleta_busqueda, entrenador, rutina

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('rutina', rutina, name='Rutinas'),
    path('buscar', buscar, name='Buscar'),
    path('atletas', atleta, name='Atletas'),
    path('atletas/add', atleta_alta, name='Formulario de Atletas'),
    path('atletas/delete/<id_atleta>', atleta_delete, name = 'Borrar Atletas'),
    path('atletas/update/<id_atleta>', atleta_update, name= 'Actualizar Atletas'),
    path('atletas/buscar', atleta_busqueda, name='Busqueda de Atletas'),
    path('entrenadores', entrenador, name='Entrenadores'),
]