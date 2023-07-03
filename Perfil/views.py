from django.shortcuts import render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from Usuarios.models import Usuario
from Papeleta.models import PapeletaPrestamo

@usuarios_permitidos(allowed_roles=['Administrativos', 'Usuarios'])
def user(request):
    user = request.user
    papeleta = PapeletaPrestamo.objects.all()
    context = {'user': user, 'papeleta': papeleta}
    return render(request, "user.html", context)
