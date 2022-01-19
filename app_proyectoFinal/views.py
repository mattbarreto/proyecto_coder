from unittest import result
from django.shortcuts import render

# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')


def atleta(request):

    return render(request, 'atletas.html')


def entrenador(request):

    return render(request, 'entrenadores.html')


def rutina(request):

    return render(request, 'rutinas.html')