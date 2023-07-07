from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.papeleta),
    path('usuarios/', views.users),
    path('verprestamos/', views.papeleta, name="verPapeleta"),
    path('registrarUsuario', views.registrarUsuario),
    path('libros/', views.libros),
    path('anadirLibro', views.anadirLibro),
    path('eliminarLibro/<int:id>', views.eliminarLibro, name="eliminarLibro"),   
    path('eliminarUsuario/<int:id>', views.eliminarUsuario, name="eliminarUsuario"), 
    path('editarLibro/<int:id>', views.editarLibro, name="editarLibro"),     
    path('edicionLibro', views.edicionLibro, name="edicionLibro"),     
    path('eliminarPrestamo/<int:id>', views.eliminarPrestamo, name="eliminarPrestamo"),
    path('buscarLibro/', views.busqueda, name='buscarLibro'),
]
