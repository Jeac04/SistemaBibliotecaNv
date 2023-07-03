from django.shortcuts import render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from Consulta.models import Libro

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def gestionar_libros(request, Ingenieria=None, id=None):
    if Ingenieria:
        if id:
            libro = Libro.objects.get(id=id)
            context = {'libro': libro}
            template_name = f'{Ingenieria.lower()}1.html'
        else:
            libros = Libro.objects.filter(Ingenieria=Ingenieria)
            context = {'libros': libros}
            template_name = f'{Ingenieria.lower()}.html'
    else:
        context = {}
        template_name = 'gestionar_libros.html'

    return render(request, template_name, context)
