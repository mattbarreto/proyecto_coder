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
    # ENTRENADORES
    path('entrenadores', EntrenadoresListViews.as_view(), name='Entrenadores'),
    path('entrenadores_add', EntrenadoresCreateView.as_view(), name='Entrenadores_formulario'),
    path('entrenadores/update/<pk>', EntrenadoresUpdateView.as_view(), name='actualizar Entrenadores'),
    path('entrenadores/view/<pk>', EntrenadoresDetailView.as_view(), name='Entrenadores_view'),
    # RUTINAS
    path('rutinas', RutinasListView.as_view(), name='Rutinas'),
    path('rutinas/detalle/<pk>', RutinasDetailView.as_view(), name='Detalle de Rutinas'),
    path('rutinas/add', RutinasCreateView.as_view(), name='Formulario de Rutinas'),
    path('rutinas/update/<pk>', RutinasUpdateView.as_view(), name='Actualizar Rutinas'),
    path('rutinas/delete/<pk>', RutinasDeleteView.as_view(), name='Borrar Rutinas'),
    path('rutinas/buscar', rutinas_busqueda, name='Busqueda de Rutinas'),
    path('buscar_rutina', buscar_rutina, name='Buscar Rutinas'),
]