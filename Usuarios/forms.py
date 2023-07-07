from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario
from django.core.validators import RegexValidator
from django.contrib.auth.password_validation import validate_password

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    carrera = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),
    ('Ingeniería en Software', 'IngenierÍa en Software'), 
    ('IngenierÍa en Sistemas Automotrices', 'IngenierÍa en Sistemas Automotrices'),
    ('IngenierÍa en Financiera', 'IngenierÍa en Financiera'),
    ('IngenierÍa en Mecatrónica', 'IngenierÍa en Mecatrónica'),
    ('IngenierÍa en Nanotecnología', 'IngenierÍa en Nanotecnología'),
    ('IngenierÍa en Animación y Efectos Visuales', 'IngenierÍa en Animación y Efectos Visuales'),
    ('IngenierÍa Agorindustrial', 'IngenierÍa Agorindustrial'),
    ('IngenierÍa en Energía', 'IngenierÍa en Energía'),
    ('IngenierÍa en Tecnología Ambiental', 'IngenierÍa en Tecnología Ambiental'),
    ('IngenierÍa en Logísta y Transporte', 'IngenierÍa en Logísta y Transporte')])
    turno = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('Matutino', 'Matutino'), ('Vespertino', 'Vespertino')])
    grupo = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('A', 'A'), ('B', 'B')])
    cuatrimestre = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('1', '1'), ('2', '2'),
    ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'),('8', '8'),('9', '9'),('10', '10')])
    rol= forms.ChoiceField(choices=[('opcion0', 'Elige una opción'), ('Estudiante', 'Estudiante'), ('P.A', 'P.A'), ('P.T.C', 'P.T.C')])
    email = forms.EmailField(label='Correo electrónico', help_text='Debe ser un correo de @uptapachula.edu.mx')
   
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'carrera', 'turno', 'grupo', 'cuatrimestre', 'rol', 'password1', 'password2')