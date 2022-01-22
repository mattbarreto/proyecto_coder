import email
from unittest import result
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app_proyectoFinal.models import Atleta
from app_proyectoFinal.forms import atleta_create

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

def buscar(request):

    respuesta = f"El resultado de su busqueda es: {request.GET['nombre']} {request.GET['apellido']}"
    return HttpResponse(respuesta)