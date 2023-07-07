from django.shortcuts import render, redirect
from Consulta.models import Libro
from Usuarios.models import Usuario
from Papeleta.models import PapeletaPrestamo
from SistemadeGestiondeBiblioteca.decorators import  usuarios_permitidos, admin_only

def admin(request):
    return render(request, "panel.html")

def busqueda(request):
    codigo_buscar = request.GET.get('codigo')

    try:
        libro = Libro.objects.get(codigo=codigo_buscar)
    except Libro.DoesNotExist:
        libro = None

    return render(request, 'libros.html', {'libro': libro, 'codigo_buscar': codigo_buscar})



def users(request):
    usuariosregistrados=Usuario.objects.all()
    return render(request, "usuarios.html", {"usuarios":usuariosregistrados})



def registrarUsuario(request):
    username=request.POST['txtMatricula']
    nombre=request.POST['txtNombre']
    carrera=request.POST['txtCarrera']
    grupo=request.POST['txtGrupo']
    turno=request.POST['txtTurno']
    cuatrimestre=request.POST['txtCuatrimestre']
    email=request.POST['txtCorreo']
    password=request.POST['txtpassword']
    
    
    usuariosregistrados=Usuario.objects.create(username=username, nombre=nombre, 
        carrera=carrera, grupo=grupo, turno= turno, cuatrimestre=cuatrimestre, email=email,
        password=password)
    
    return redirect ("usuarios/")



def eliminarUsuario(request, id):
    usuario = Usuario.objects.get(id=id)
    context = {
        'usuario':usuario
    }
    usuario.delete()

    return redirect('/usuarios')



def libros(request):
    inventariolibros=Libro.objects.all().order_by('Codigo')
    return render(request, "libros.html", {"libros": inventariolibros})


def papeleta(request):
    prestamosregistrados=PapeletaPrestamo.objects.all()
    print(prestamosregistrados)
    return render(request, "panel.html", {"prestamo": prestamosregistrados})


def anadirLibro(request):
    Codigo=request.POST['txtCodigo']
    Isbn=request.POST['txtIsbn']
    Nombre=request.POST['txtNombre']
    Ejemplares=request.POST['txtEjemplares']
    Paginas=request.POST['txtPaginas']
    Autor=request.POST['txtAutor']
    Editorial=request.POST['txtEditorial']
    Edicion=request.POST['txtEdicion']
    Ingenieria=request.POST['txtIngenieria']
    Descripcion=request.POST['txtDescripcion']
    
    aLibros=Libro.objects.create(Codigo=Codigo, Isbn=Isbn, Nombre=Nombre, 
        Ejemplares=Ejemplares, Paginas=Paginas, Autor=Autor, Editorial=Editorial, Edicion=Edicion, Ingenieria=Ingenieria, Descripcion=Descripcion)
    return redirect ("libros/")


def eliminarLibro(request ,id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }
    libro.delete()

    return redirect('/libros')

def editarLibro(request ,id):
    libro = Libro.objects.get(id=id)
    context = {
        'libro':libro
    }

    return render(request, "editarLibro.html", context)

def edicionLibro(request):
    id=request.POST['id']
    Codigo=request.POST['txtCodigo']
    Isbn=request.POST['txtIsbn']
    Nombre=request.POST['txtNombre']
    Ejemplares=request.POST['txtEjemplares']
    Paginas=request.POST['txtPaginas']
    Autor=request.POST['txtAutor']
    Editorial=request.POST['txtEditorial']
    Edicion=request.POST['txtEdicion']
    Ingenieria=request.POST['txtIngenieria']
    Descripcion=request.POST['txtDescripcion']
    
    libro = Libro.objects.get(id=id)
    
    libro.Codigo=Codigo
    libro.Isbn=Isbn
    libro.Nombre=Nombre
    libro.Ejemplares=Ejemplares
    libro.Paginas=Paginas
    libro.Autor=Autor
    libro.Editorial=Editorial
    libro.Edicion=Edicion
    libro.Ingenieria=Ingenieria
    libro.Descripcion=Descripcion
    libro.save()
    
    return redirect ("libros/")

def eliminarPrestamo(request ,id):
    prestamo = PapeletaPrestamo.objects.get(id=id)
    context = {
        'prestamo': prestamo
    }
    prestamo.delete()

    return redirect('/panel')