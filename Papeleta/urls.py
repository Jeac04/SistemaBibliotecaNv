from django.urls import path
from . import views

urlpatterns = [
    path('gestionar-papeleta/', views.gestionar_papeleta, name='papeleta'),
]
