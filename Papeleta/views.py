from django.shortcuts import render, redirect
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from django.shortcuts import render, redirect
from Papeleta.models import PapeletaPrestamo
from Consulta.models import Libro
from datetime import datetime, timedelta


@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def gestionar_papeleta(request, id=None):
    if request.method == 'POST':
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
        observaciones = request.POST['txtObservaciones']

        fecha_devolucion = datetime.strptime(fecha_devolucion, "%B %d, %Y").strftime("%Y-%m-%d")
        fecha_prestamo = datetime.strptime(fecha_prestamo, "%B %d, %Y").strftime("%Y-%m-%d")

        prestamos_registrados = PapeletaPrestamo.objects.create(
            folio=folio,
            nombre_solicitante=nombre_solicitante,
            matricula=matricula,
            ingenieria=ingenieria,
            cuatrimestre=cuatrimestre,
            turno=turno,
            rol=rol,
            codigo=codigo,
            titulo=titulo,
            autor=autor,
            fecha_prestamo=fecha_prestamo,
            fecha_devolucion=fecha_devolucion,
            observaciones=observaciones
        )

        return redirect('papeleta.html')
    else:
        if id:
            libro = Libro.objects.get(id=id)
            fecha_actual = datetime.now()
            fecha_nueva = fecha_actual.date()
            fecha_devolucion = fecha_nueva + timedelta(days=3)
            context = {
                'libro': libro,
                'fecha_actual': fecha_nueva,
                'fechaDevolucion': fecha_devolucion,
            }
            return render(request, "papeleta.html", context)
        else:
            fecha_actual = datetime.now()
            fecha_nueva = fecha_actual.date()
            context = {
                'fecha_nueva': fecha_nueva
            }
            return render(request, "papeleta.html", context)
