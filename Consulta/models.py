from django.db import models

class Libro(models.Model):
    Codigo=models.CharField(max_length=10, null=True)
    Isbn=models.CharField(max_length=50, null=True)
    Nombre=models.CharField(max_length=200, null=True)
    Ejemplares=models.IntegerField(null=True)
    Paginas=models.IntegerField(null=True)
    Autor=models.CharField(max_length=30, null=True)
    Editorial=models.CharField(max_length=50, null=True)
    Edicion=models.CharField(max_length=50, null=True)
    Ingenieria=models.CharField(max_length=70, null=True)
    Descripcion= models.CharField(max_length=300, null=True)
    

