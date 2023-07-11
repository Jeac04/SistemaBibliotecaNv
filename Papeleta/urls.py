from django.urls import path,reverse
from . import views

urlpatterns = [
    path('generarprestamo/<int:id>', views.generar, name='generarprestamo'),
    path('registrarPapeleta', views.registrarPapeleta, name='registrarPapeleta'),
    path('fechaActual', views.fecha_actual, name='fechaActual'),
    path('fechaDevolucion', views.fecha_devolucion, name='fechaDevolucion'),
    path('confirmacion/<str:folio>/<str:codigo_papeleta>/', views.paginaConfirmacion, name='pagina_confirmacion'),
]
