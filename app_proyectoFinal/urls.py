from django.urls import path
from app_proyectoFinal.views import atletas_ls, atletaCreateView, atletaDetailView, atletaDeleteView, atletaListView, atletaUpdateView, inicio, atleta_delete, atleta_update ,atleta_busqueda, entrenador, rutina

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('rutina', rutina, name='Rutinas'),
    # path('atletas', atleta, name='Atletas'),
    # path('atletas/add', atleta_alta, name='Formulario de Atletas'),
    # path('atletas/delete/<id_atleta>', atleta_delete, name = 'Borrar Atletas'),
    # path('atletas/update/<id_atleta>', atleta_update, name= 'Actualizar Atletas'),
    path('atletas', atletaListView.as_view(), name='Atletas'),
    path('atletas/detalle/<pk>', atletaDetailView.as_view(), name='Detalle Atletas'),
    path('atletas/add', atletaCreateView.as_view(), name='Formulario de Atletas'),
    path('atletas/update/<pk>', atletaUpdateView.as_view(), name='Actualizar Atletas'),
    path('atletas/delete/<pk>', atletaDeleteView.as_view(), name='Borrar Atletas'),
    path('atletas/buscar', atleta_busqueda, name='Busqueda de Atletas'),
    path('atletas/listar_busqueda', atletas_ls, name='Search'),
    path('entrenadores', entrenador, name='Entrenadores'),
]