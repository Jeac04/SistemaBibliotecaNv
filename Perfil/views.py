from django.shortcuts import render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos
from Papeleta.models import PapeletaPrestamo

@usuarios_permitidos(allowed_roles=['Administratidores', 'Usuarios'])
def user(request):
    user = request.user
    papeleta = PapeletaPrestamo.objects.filter(usuario=user.id)
    context = {'user': user, 'papeleta': papeleta}
    return render(request, "user.html", context)
