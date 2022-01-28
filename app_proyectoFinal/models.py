from django.db.models import Model
from django.db.models.fields import CharField, EmailField, DateField, DecimalField, IntegerField

class Atleta(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    disciplina = CharField(max_length=40)
    fecha_de_nacimiento = DateField()
    ciudad_de_nacimiento = CharField(max_length=30)
    pais_de_nacimiento = CharField(max_length=30)
    altura = DecimalField()
    peso = DecimalField()
    email = EmailField()

    def __str__(self):
        return f'Atleta: {self.nombre} {self.apellido} Disciplina: {self.disciplina} Altura: {self.altura} Peso: {self.peso} Pais de origen: {self.pais_de_nacimiento} Email: {self.email}'
class Entrenador(Model):

    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    fecha_de_nacimiento = DateField()
    estudios = CharField(max_length=50)
    especialidad = CharField(max_length=40)
    email = EmailField()

    def __str__(self):
        return f'Entrenador: {self.nombre} {self.apellido} Estudios: {self.estudios} Especialidad: {self.especialidad} Email: {self.email}'

class Rutina(Model):

    nombre = CharField(max_length=40)
    fecha_inicio = DateField()
    intensidad = CharField(max_length=10)
    ejercicio_1 = CharField(max_length=40)
    ejercicio_2 = CharField(max_length=40)
    ejercicio_3 = CharField(max_length=40)
    ejercicio_4 = CharField(max_length=40)
    ejercicio_5 = CharField(max_length=40)
    ejercicio_6 = CharField(max_length=40)
    ejercicio_7 = CharField(max_length=40)
    duracionPorEjercicio = IntegerField()
    descansoEntreEjercicio = IntegerField()
    rondas = IntegerField()

    def __str__(self):
        return f'Rutina: {self.nombre} Intensidad: {self.intensidad} Ejercicio 1: {self.ejercicio_1}'