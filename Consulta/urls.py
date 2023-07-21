from django.urls import path
from . import views

urlpatterns = [
    path('software/', views.software),
    path('is1/<int:id>', views.software1),
    path('cienciasbasicas/', views.cb),
    path('cb1/<int:id>', views.cb1),
    path('ingles/', views.ingles),
    path('igl1/<int:id>', views.ingles1),
    path('nanotecnologia/', views.nano),
    path('in1/<int:id>', views.nano1),
    path('energia/', views.energia),
    path('ie1/<int:id>', views.energia1),
    path('sistemasautomotirces/', views.automotriz),
    path('isa1/<int:id>', views.automotirz1),
    path('mecatronica/', views.mecatronica),
    path('im1/<int:id>', views.mecatronica1),
    path('financiera/', views.financiera),
    path('if1/<int:id>', views.financiera1),
    path('tecnologiaambiental/', views.ambiental),
    path('ita1/<int:id>', views.ambiental1),
    path('logisticaytransporte/', views.logistica),
    path('ilt1/<int:id>', views.logistica1),
    path('agroindustrial/', views.agro),
    path('iai1/<int:id>', views.agro1),
    path('animacionyefectosvisuales/', views.animacion),
    path('iaev1/<int:id>', views.animacion1),
]
