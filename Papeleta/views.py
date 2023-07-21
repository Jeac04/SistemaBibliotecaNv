from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from django.shortcuts import render, redirect
from Papeleta.models import PapeletaPrestamo
from Consulta.models import Libro
from datetime import datetime, timedelta
import shortuuid
import random
from Usuarios.models import Usuario

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def fecha_actual(request):

    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual.date()
    print(fecha_nueva)
    context= {
        'fecha_nueva': fecha_nueva
    }
    print(fecha_nueva)
    return render(request, "papeleta.html", context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def fecha_devolucion(request):
    
    fecha_actual = datetime.now()
    fecha_nueva = fecha_actual.date()
    fechaDevolucion= fecha_nueva + timedelta(days=3)
    print(fechaDevolucion)
    context= {
        'fechadevolucion': fechaDevolucion
    }
    print(fechaDevolucion)
    return render(request, "papeleta.html" , context)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def generar(request):
        n_random= random.randint(0, 9999)
        folio = "23" + str(n_random).zfill(4)
        libro = Libro.objects.get(id=id)
        fecha_actual = datetime.now()
        fecha_nueva = fecha_actual.date()
        fechaDevolucion= fecha_nueva + timedelta(days=3)
        # print(fecha_nueva)
        context = {
            'libro':libro,
            'fecha_actual': fecha_nueva,
            'fechaDevolucion': fechaDevolucion,
            'folio': folio,
        }
        return render(request, "papeleta.html")

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def registrarPapeleta(request):
    user = Usuario.objects.get(id=request.user.id)
    print(user)
    print(request)
    codigo_papeleta = shortuuid.uuid()[:5]
    folio = request.POST['txtFolio']
    nombre_solicitante = request.POST['txtNombre']
    matricula = request.POST['txtMatricula']
    ingenieria = request.POST['txtIngenieria']
    cuatrimestre = request.POST['txtCuatrimestre']
    turno = request.POST['txtTurno']
    rol = request.POST['txtRol']
    codigo = request.POST['txtCodigo']
    titulo = request.POST['txtTitulo']
    autor = request.POST['txtAutor']
    fecha_prestamo = request.POST['txtFechaprestamo']
    fecha_devolucion = request.POST['txtFechadevolucion']
    fecha_devolucion = datetime.strptime(fecha_devolucion, "%B %d, %Y").strftime("%Y-%m-%d")
    fecha_prestamo = datetime.strptime(fecha_prestamo, "%B %d, %Y").strftime("%Y-%m-%d")
    observaciones = request.POST['txtObservaciones']
    context= {
        'Mensaje': 'Este libro solo está disponible para consulta.'
    }
    
    libro = get_object_or_404(Libro, Codigo=codigo)
    libro.Ejemplares = libro.Ejemplares - 1
    libro.save()
    print(libro.Ejemplares)
    if libro.Ejemplares == 1:
        messages.warning(request, 'Este libro solo está disponible para consulta.')
     
    prestamosregistrados = PapeletaPrestamo.objects.create(
        codigo_papeleta=codigo_papeleta, folio=folio, nombre_solicitante=nombre_solicitante, matricula=matricula,
        ingenieria=ingenieria, cuatrimestre=cuatrimestre, turno=turno, rol=rol, codigo=codigo, titulo=titulo, autor=autor,
        fecha_prestamo=fecha_prestamo, fecha_devolucion=fecha_devolucion, observaciones=observaciones, usuario=user
    )

    return redirect('pagina_confirmacion', folio=folio, codigo_papeleta=codigo_papeleta)

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def paginaConfirmacion(request, folio, codigo_papeleta):
    try:
        papeleta = PapeletaPrestamo.objects.get(folio=folio, codigo_papeleta=codigo_papeleta)
    except PapeletaPrestamo.DoesNotExist:
        return redirect('pagina_error')
    context= {
       'papeleta' : papeleta 
    }
    
    return render(request, 'confirmacion.html', context )


