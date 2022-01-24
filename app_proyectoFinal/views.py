from dataclasses import field
import email
from mailbox import NoSuchMailboxError
from re import A, template
from unittest import result
from winreg import DeleteValue
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q 
from app_proyectoFinal.models import Atleta
from app_proyectoFinal.forms import atleta_create

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')


def atleta(request):

    return render(request, 'atletas.html',
    {'lista_atletas': Atleta.objects.all()})


def entrenador(request):

    return render(request, 'entrenadores.html')


def rutina(request):

    return render(request, 'rutinas.html')

def atleta_alta(request):

    if request.method=='POST':
        formulario_atletas = atleta_create(request.POST)
        
        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data
            
            Atleta.objects.create(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                edad=data['edad'], 
                altura=data['altura'], 
                peso=data['peso'], 
                email=data['email']
                )
            return redirect('Atletas')
    else:
        formulario_atletas = atleta_create()

    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})

def atleta_delete(request, id_atleta):
    
    atleta = Atleta.objects.get(id=id_atleta)
    atleta.delete()
    return redirect('Atletas')

def atleta_update(request, id_atleta):
    atleta = Atleta.objects.get(id=id_atleta)

    if request.method == 'POST':
        formulario_atletas = atleta_create(request.POST)

        if formulario_atletas.is_valid():
            data = formulario_atletas.cleaned_data
                
            atleta.nombre = data['nombre']
            atleta.apellido=data['apellido']
            atleta.edad=data['edad']
            atleta.altura=data['altura']
            atleta.peso=data['peso']
            atleta.email=data['email']

            atleta.save()

            return redirect('Atletas')

    else:
        formulario_atletas = atleta_create(model_to_dict(atleta))
        
    return render(request, 'atletas_form.html', {'formulario_at': formulario_atletas})

def atleta_busqueda(request):

    return render(request, 'atletas_busqueda.html')

def atletas_ls(request):
    
    if request.GET['apellido']:
        
        apellido_buscado = request.GET['apellido']
        apellido_atleta = Atleta.objects.filter(apellido__icontains=apellido_buscado)

        return render(request, 'atletas_resultados_ls.html', {'apellido_atleta': apellido_atleta, 'query': apellido_buscado})

    else:

        respuesta = 'No enviaste datos'
        return HttpResponse(respuesta)


    # if apellido_atleta:
        
    #     atleta = Atleta.objects.filter(apellido=apellido_atleta)

    #     return render(request, 'atletas_search.html', {
    #     'apellido': apellido_atleta,
    #     'nombre': atleta,
    #     })

    # else:

    #     respuesta = 'No enviaste datos'
    #     return HttpResponse(respuesta)

    # return HttpResponse (f"Usted ha buscado al atleta {request.GET['apellido']}")

class atletaListView(ListView):
    model = Atleta
    template_name = 'atletas.html'
    context_object_name = 'lista_atletas'

class atletaDetailView(DetailView):
    model = Atleta
    template_name = 'atletas_ver.html'

class atletaCreateView(CreateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'edad', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'

class atletaUpdateView(UpdateView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    fields = ['nombre', 'apellido', 'edad', 'altura', 'peso', 'email']
    template_name = 'atletas_formulario.html'

class atletaDeleteView(DeleteView):
    model = Atleta
    success_url = reverse_lazy('Atletas')
    template_name = 'atletas_confirm_delete.html'