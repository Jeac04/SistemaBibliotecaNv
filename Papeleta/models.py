from django.db import models
from datetime import datetime

class PapeletaPrestamo(models.Model):
    folio = models.CharField(max_length=50, unique=True)
    codigo_papeleta=models.CharField(max_length=10, unique=True)
    nombre_solicitante = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20)
    ingenieria = models.CharField(max_length=70)
    cuatrimestre = models.CharField(max_length=20)
    turno = models.CharField(max_length=20)
    rol = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=40)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank= True, null= True)
    observaciones = models.CharField(max_length=200)
