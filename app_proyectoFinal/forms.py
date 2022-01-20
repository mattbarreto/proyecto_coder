from django.forms import Form, IntegerField, CharField, EmailField, FloatField

class atleta_form(Form):
    nombre = CharField()
    apellido = CharField()
    edad = IntegerField()
    altura = FloatField()
    peso = FloatField()
    email = EmailField()