from django.shortcuts import redirect, render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from Consulta.models import Libro

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def cb(request):
    libros=Libro.objects.filter(Ingenieria='Ciencias Básicas')
    context= {'libros':libros}
    return render(request, "cb.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def cb1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "cb1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def ingles(request):
    libros=Libro.objects.filter(Ingenieria='Inglés')
    context= {'libros':libros}
    return render(request, "igl.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def ingles1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "igl1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def software(request):
    
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Software')
    context= {'libros':libros}
    return render(request, "is.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def software1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "is1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def automotriz(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Sistemas Automotrices')
    context= {'libros':libros}
    return render(request, "isa.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def automotirz1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "isa1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def energia(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Energía')
    context= {'libros':libros}
    return render(request, "ie.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def energia1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "ie1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def mecatronica(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería Mecatrónica')
    context= {'libros':libros}
    return render(request, "im.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def mecatronica1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "ie1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def financiera(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería Financiera')
    context= {'libros':libros}
    return render(request, "if.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def financiera1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "if1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def mecatronica1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "im1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def ambiental(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Tecnología Ambiental')
    context= {'libros':libros}
    return render(request, "ita.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def ambiental1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "ita1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def nano(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Nanotecnología')
    context= {'libros':libros}
    return render(request, "in.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def nano1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "in1.html", context)
    
@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def logistica(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería Logistica y Transporte')
    context= {'libros':libros}
    return render(request, "ilt.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def logistica1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "ilt1.html", context)
 
@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios']) 
def animacion(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería en Animación y Efectos Visuales')
    context= {'libros':libros}
    return render(request, "iaev.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def animacion1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "iaev1.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios']) 
def agro(request):
    libros=Libro.objects.filter(Ingenieria='Ingeniería Agroindustrial')
    context= {'libros':libros}
    return render(request, "iai.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def agro1(request, id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    print(libro)
    return render(request, "iai1.html", context)
    

