from django.urls import path
from . import views

urlpatterns = [
    path('gestionar-libros/<str:Ingenieria>/<int:id>/', views.gestionar_libros, name='gestionar_libros'),
]
