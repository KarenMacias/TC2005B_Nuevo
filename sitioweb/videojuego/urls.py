from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('inicio',views.inicio,name='inicio'),
    path('acercaDe',views.acercaDe,name='acercaDe'),
    path('instrucciones',views.instrucciones,name='instrucciones'),
    path('estadisticas',views.estadisticas,name='estadisticas'),
    path('reto',views.reto,name='reto'),
    path('contactanos',views.contactanos,name='contactanos'),
]