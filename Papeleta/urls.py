from django.urls import path
from . import views

urlpatterns = [
    path('generarprestamo/<int:id>', views.generar, name='generarprestamo'),
    path('registrarPapeleta', views.registrarPapeleta, name='registrarPapeleta'),
    path('fechaActual', views.fecha_actual, name='fechaActual'),
    path('fechaDevolucion', views.fecha_devolucion, name='fechaDevolucion'),
]
