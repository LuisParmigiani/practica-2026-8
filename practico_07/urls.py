# Configuración de rutas (URLs) para la aplicación de Socios

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_socios, name='lista_socios'),
    path('crear/', views.crear_socio, name='crear_socio'),
    path('modificar/<int:socio_id>/', views.modificar_socio, name='modificar_socio'),
    path('eliminar/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),
]
