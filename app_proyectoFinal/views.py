import email
from unittest import result
from django.shortcuts import redirect, render
from app_proyectoFinal.models import Atleta

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')


def atleta(request):

    return render(request, 'atletas.html',
    {'atleta': Atleta.objects.all()})


def entrenador(request):

    return render(request, 'entrenadores.html')


def rutina(request):

    return render(request, 'rutinas.html')

def atletas_form(request):

    if request.method=='POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        edad = request.POST['edad']
        altura = request.POST['altura']
        peso = request.POST['peso']
        email = request.POST['email']
        Atleta.objects.create(nombre=nombre, apellido=apellido, edad=edad, altura=altura, peso=peso, email=email)
        return redirect('Atletas')

    return render(request, 'atletas_form.html')