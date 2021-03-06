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
    def __str__(self):
        return f'Nombre y apellido: {self.nombre} {self.apellido} Edad: {self.edad} Altura: {self.altura} Peso: {self.peso} Email: {self.email}'

class Entrenador(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    email = EmailField()
    profesion = CharField(max_length=50)
    def __str__(self):
        return f'Nombre y apellido: {self.nombre} {self.apellido} Profesion: {self.profesion} Email: {self.email}'

class Rutina(Model):

    nombre = CharField(max_length=40)
    fecha_inicio = DateField()
    def __str__(self):
        return f'Rutina: {self.nombre} Fecha de inicio: {self.fecha_inicio}'