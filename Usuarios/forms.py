from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    carrera = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'IngenierÍa en Software'), 
    ('opcion2', 'IngenierÍa en Sistemas Automotrices')])
    turno = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'Matutino'), ('opcion2', 'Vespertino')])
    grupo = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'A'), ('opcion2', 'B')])
    cuatrimestre = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', '1'), ('opcion2', '2'),
    ('opcion2', '3'), ('opcion2', '4'), ('opcion2', '5'), ('opcion2', '6'), ('opcion2', '7')])
    email = forms.EmailField(label='Correo electrónico', help_text='Debe ser un correo de @uptapachula.edu.mx')

    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput,
        min_length=1,
        help_text='La contraseña debe ser de al menos 1 caracter y solo números.'
    )
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'carrera', 'turno', 'grupo', 'cuatrimestre', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 1 or not password1.isdigit():
            raise forms.ValidationError('La contraseña debe ser de al menos 1 caracter y solo números.')
        return password1

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@uptapachula.edu.mx'):
            raise forms.ValidationError('El correo debe tener la terminación @uptapachula.edu.mx')
        return email
    