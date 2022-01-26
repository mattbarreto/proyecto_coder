from django.forms import DateField, Form, IntegerField, CharField, EmailField, FloatField

class atleta_create(Form):
    nombre = CharField()
    apellido = CharField()
    edad = IntegerField()
    altura = FloatField()
    peso = FloatField()
    email = EmailField()
    
class rutinas_create(Form):

    nombre = CharField()
    fecha_inicio = DateField()
    intensidad = CharField()
    ejercicio_1 = CharField()
    ejercicio_2 = CharField()
    ejercicio_3 = CharField()
    ejercicio_4 = CharField()
    ejercicio_5 = CharField()
    ejercicio_6 = CharField()
    ejercicio_7 = CharField()
    duracionPorEjercicio = IntegerField()
    descansoEntreEjercicio = IntegerField()
    rondas = IntegerField()