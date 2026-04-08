# URL Configuration para el proyecto Django principal

from django.urls import path, include

urlpatterns = [
    path('socios/', include('practico_07.urls')),
]
