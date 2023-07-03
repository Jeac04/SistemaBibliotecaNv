from django.urls import path
from . import views

urlpatterns = [
    path('panel/', views.Panel_Administrador, name='panel'),
    path('libros/', views.Panel_Administrador, name='libros'),
]
