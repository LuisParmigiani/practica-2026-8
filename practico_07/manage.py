# Punto de entrada para ejecutar la aplicación Django
# Ejecutar con: python manage.py runserver

import os
import django
from django.conf import settings
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practico_07.settings')
    django.setup()
    
    # Para ejecutar el servidor: python -m practico_07.manage runserver
    # O más simplemente en la terminal: python manage.py runserver
