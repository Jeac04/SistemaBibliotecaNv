from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Usuario
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    carrera = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'IngenierÍa en Software'), 
    ('opcion2', 'IngenierÍa en Sistemas Automotrices'),('opcion3', 'IngenierÍa en Financiera'),('opcion4', 'IngenierÍa en Mecatrónica'),
    ('opcion5', 'IngenierÍa en Nanotecnología'),('opcion6', 'IngenierÍa en Animación y Efectos Visuales'),('opcion7', 'IngenierÍa Agorindustrial'),
    ('opcion8', 'IngenierÍa en Energía'),('opcion9', 'IngenierÍa en Tecnología Ambiental'),('opcion210', 'IngenierÍa en Logísta y Transporte')])
    turno = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'Matutino'), ('opcion2', 'Vespertino')])
    grupo = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', 'A'), ('opcion2', 'B')])
    cuatrimestre = forms.ChoiceField(choices=[('opcion0', 'Elige una Opción'),('opcion1', '1'), ('opcion2', '2'),
    ('opcion3', '3'), ('opcion4', '4'), ('opcion5', '5'), ('opcion6', '6'), ('opcion7', '7'),('opcion8', '8'),('opcion9', '9'),('opcion210', '10')])
    email = forms.EmailField(label='Correo electrónico', help_text='Debe ser un correo de @uptapachula.edu.mx')
    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput,
        validators=[
            MaxLengthValidator(8, 'La contraseña debe tener menos de 8 caracteres.'),
            MinLengthValidator(1, 'La contraseña debe tener al menos 1 carácter.'),
            RegexValidator(r'^\d+$', 'La contraseña debe contener solo dígitos.')
        ],
        help_text='La contraseña debe contener solo dígitos con una longitud menor a 8.'
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput,
        strip=False,
        help_text='Ingrese la misma contraseña para confirmar.'
    )

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombre', 'carrera', 'turno', 'grupo', 'cuatrimestre', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@uptapachula.edu.mx'):
            raise forms.ValidationError('El correo debe tener la terminación @uptapachula.edu.mx')
        return email
