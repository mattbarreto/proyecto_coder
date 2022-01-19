from django.db.models import Model
from django.db.models.fields import CharField, IntegerField, EmailField, DateField

# Create your models here.


class Atleta(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    edad= IntegerField()
    altura= IntegerField()
    peso= IntegerField()
    email = EmailField()


class Entrenador(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    email = EmailField()
    profesion = CharField(max_length=50)


class Rutina(Model):

    nombre = CharField(max_length=40)
    fecha_inicio = DateField()
