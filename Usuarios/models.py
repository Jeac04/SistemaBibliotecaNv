from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.core.validators import RegexValidator


from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=70)
    turno = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    cuatrimestre = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group, related_name='usuario_set')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_set')

    password = models.CharField(
        validators=[
            MaxLengthValidator(8),
            MinLengthValidator(1),
            RegexValidator(r'^\d+$', 'La contraseña debe contener solo dígitos.')
        ],
        max_length=128,
        help_text='Ingrese una contraseña de dígitos con una longitud menor a 8.'
    )

