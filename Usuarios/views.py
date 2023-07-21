from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from SistemadeGestiondeBiblioteca.decorators import usuario_noidentificado
from django.contrib.auth.models import Group
from .forms import RegistroForm


@usuario_noidentificado
def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, "Has creado tu cuenta")
            
            group= Group.objects.get(name='Usuarios')
            user.groups.add(group)
            
            return redirect('/login')
        
    else:
        form = RegistroForm()
    return render(request, 'singup.html', {'form': form})

@usuario_noidentificado
def loginUser(request):

    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        print(password, username)
        user= authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('/panel')
            else:
                login(request, user)
                return redirect('/')
        else: 
            context= {
                'error' : 'La Matrícula o la Contraseña son Incorrectos'
            }
            return render(request, 'login.html', context)
    else:  
        
        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect("/login")
    
    