from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=100)
    carrera = models.CharField(max_length=70)
    turno = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    cuatrimestre = models.CharField(max_length=100)
    rol= models.CharField(max_length=20, default='Usuario')
    groups = models.ManyToManyField(Group, related_name='usuario_set')
    user_permissions = models.ManyToManyField(Permission, related_name='usuario_set')


