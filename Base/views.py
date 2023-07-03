from django.shortcuts import render
from SistemadeGestiondeBiblioteca.decorators import usuarios_permitidos

@usuarios_permitidos(allowed_roles=['Usuarios'])
def home(request):
    return render(request, "home.html")
