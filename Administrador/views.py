from django.shortcuts import render, redirect
from Consulta.models import Libro
from Usuarios.models import Usuario
from Papeleta.models import PapeletaPrestamo
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos, admin_only

def Panel_Administrador(request):
    if request.method == 'POST':
        # Registrar usuario
        if 'txtMatricula' in request.POST:
            username = request.POST['txtMatricula']
            nombre = request.POST['txtNombre']
            carrera = request.POST['txtCarrera']
            grupo = request.POST['txtGrupo']
            turno = request.POST['txtTurno']
            cuatrimestre = request.POST['txtCuatrimestre']
            email = request.POST['txtCorreo']
            password = request.POST['txtpassword']
            
            Usuario.objects.create(username=username, nombre=nombre, carrera=carrera, grupo=grupo, turno=turno,
                                   cuatrimestre=cuatrimestre, email=email, password=password)
            return redirect('/PanelAdministrador')

        # Eliminar usuario
        elif 'eliminar-usuario' in request.POST:
            usuario_id = request.POST['eliminar-usuario']
            Usuario.objects.filter(id=usuario_id).delete()
            return redirect('/PanelAdministrador')

        # Añadir libro
        elif 'txtCodigo' in request.POST:
            Codigo = request.POST['txtCodigo']
            Isbn = request.POST['txtIsbn']
            Nombre = request.POST['txtNombre']
            Ejemplares = request.POST['txtEjemplares']
            Paginas = request.POST['txtPaginas']
            Autor = request.POST['txtAutor']
            Editorial = request.POST['txtEditorial']
            Edicion = request.POST['txtEdicion']
            Ingenieria = request.POST['txtIngenieria']
            Descripcion = request.POST['txtDescripcion']
            
            Libro.objects.create(Codigo=Codigo, Isbn=Isbn, Nombre=Nombre, Ejemplares=Ejemplares, Paginas=Paginas,
                                 Autor=Autor, Editorial=Editorial, Edicion=Edicion, Ingenieria=Ingenieria,
                                 Descripcion=Descripcion)
            return redirect('/PanelAdministrador')

        # Eliminar libro
        elif 'eliminar-libro' in request.POST:
            libro_id = request.POST['eliminar-libro']
            Libro.objects.filter(id=libro_id).delete()
            return redirect('/PanelAdministrador')

        # Editar libro
        elif 'editar-libro' in request.POST:
            libro_id = request.POST['editar-libro']
            libro = Libro.objects.get(id=libro_id)
            context = {'libro': libro}
            return render(request, 'editarLibro.html', context)

        # Actualizar libro editado
        elif 'id' in request.POST:
            id = request.POST['id']
            Codigo = request.POST['txtCodigo']
            Isbn = request.POST['txtIsbn']
            Nombre = request.POST['txtNombre']
            Ejemplares = request.POST['txtEjemplares']
            Paginas = request.POST['txtPaginas']
            Autor = request.POST['txtAutor']
            Editorial = request.POST['txtEditorial']
            Edicion = request.POST['txtEdicion']
            Ingenieria = request.POST['txtIngenieria']
            Descripcion = request.POST['txtDescripcion']
            
            libro = Libro.objects.get(id=id)
            libro.Codigo = Codigo
            libro.Isbn = Isbn
            libro.Nombre = Nombre
            libro.Ejemplares = Ejemplares
            libro.Paginas = Paginas
            libro.Autor = Autor
            libro.Editorial = Editorial
            libro.Edicion = Edicion
            libro.Ingenieria = Ingenieria
            libro.Descripcion = Descripcion
            libro.save()
            return redirect('/PanelAdministrador')

    # Obtener datos para mostrar en la vista
    usuariosregistrados = Usuario.objects.all()
    inventariolibros = Libro.objects.all().order_by('Codigo')
    prestamosregistrados = PapeletaPrestamo.objects.all()

    context = {
        'usuarios': usuariosregistrados,
        'libros': inventariolibros,
        'prestamo': prestamosregistrados
    }
    return render(request, 'panel.html', context)
