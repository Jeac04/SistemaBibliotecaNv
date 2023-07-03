from django.urls import path
from . import views

urlpatterns = [
    path('PanelAdministrador', views.Panel_Administrador, name='PanelAdministrador'),
]
