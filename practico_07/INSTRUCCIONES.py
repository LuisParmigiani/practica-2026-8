#!/usr/bin/env python
"""
INSTRUCCIONES PASO A PASO PARA EJECUTAR DJANGO

Este archivo explica cómo poner en marcha la aplicación.
"""

# ============================================================================
# PASO 1: Verificar que tienes Django instalado
# ============================================================================
# En tu terminal (asegúrate tener el venv activado):
# 
#   pip install django
#

# ============================================================================
# PASO 2: Crear estructura del proyecto Django completa
# ============================================================================
# La estructura debe ser así:
#
# /Users/agus/Developer/practica-2026-8/
# ├── practico_05/              # Módulo con clase Socio
# ├── practico_06/              # Módulo con NegocioSocio
# ├── practico_07/              # ← TU APLICACIÓN DJANGO
# │   ├── __init__.py
# │   ├── forms.py
# │   ├── views.py
# │   ├── urls.py
# │   ├── settings.py
# │   ├── manage.py
# │   ├── templates/            # ← TEMPLATES HTML
# │   │   ├── base.html
# │   │   ├── lista_socios.html
# │   │   ├── formulario_socio.html
# │   │   └── formulario_modificar.html  ← ¡TÚ DEBES COMPLETAR ESTO!
# │   └── README.md
# ├── manage_project.py         # ← Para ejecutar el servidor completo
# ├── proyecto_urls.py
# └── ...

# ============================================================================
# PASO 3: COMPLETAR funciones_modificar.html
# ============================================================================
#
# Abre: practico_07/templates/formulario_modificar.html
# 
# Verás que tiene un comentario TODO. Debes completarlo con:
# 
# 1. Campo DNI (readonly - no editable)
#    <input type="number" ... readonly>
# 
# 2. Campo Nombre (editable)
# 
# 3. Campo Apellido (editable)
# 
# 4. Botones: "Aceptar" y "Cancelar"
#
# Usa como referencia: formulario_socio.html

# ============================================================================
# PASO 4: Opción A - Ejecutar con Django Development Server
# ============================================================================
#
#  cd /Users/agus/Developer/practica-2026-8
#  python -m django runserver --settings=practico_07.settings
#
# Luego abre: http://localhost:8000/socios/

# ============================================================================
# PASO 4: Opción B - Ejecutar con manage.py tradicional
# ============================================================================
#
# 1. Crea un archivo "django_manage.py" en la raíz del proyecto:
#
#    import os
#    import sys
#    from django.core.management import execute_from_command_line
#
#    if __name__ == '__main__':
#        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practico_07.settings')
#        execute_from_command_line(sys.argv)
#
# 2. Ejecuta:
#    python django_manage.py runserver
#

# ============================================================================
# PASO 5: Probar la aplicación
# ============================================================================
#
# 1. Abre http://localhost:8000/socios/
# 2. Verás una tabla vacía con botón "Alta"
# 3. Prueba todas las funcionalidades:
#    - Click en "Alta" → Crear un nuevo socio
#    - Click en "Modificar" → AQUÍ PRUEBAS TU TEMPLATE
#    - Click en "Baja" → Eliminar un socio
#    - Verifica que los errores se muestran correctamente

print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                 RESUMEN: ESTRUCTURA DE LA SOLUCIÓN                         ║
╚════════════════════════════════════════════════════════════════════════════╝

✅ YA COMPLETADO:
  • forms.py          → Formularios Django con validaciones
  • views.py          → Las 4 vistas (lista, crear, modificar, eliminar)
  • urls.py           → Rutas (URLs)
  • settings.py       → Configuración Django
  • base.html         → Template base con Bootstrap
  • lista_socios.html → Tabla de socios (MUY IMPORTANTE: aquí están los botones)
  • formulario_socio.html → Formulario para crear socio

⚠️  TÚ DEBES COMPLETAR:
  • formulario_modificar.html → Formulario para modificar socio

═════════════════════════════════════════════════════════════════════════════

DIAGRAMA DEL FLUJO:
═════════════════════════════════════════════════════════════════════════════

                           USUARIO
                              ↓
                    http://localhost:8000/socios/
                              ↓
              ┌─────────────────┼───────────────────┐
              ↓                 ↓                     ↓
            [Alta]        [Modificar]            [Baja]
              ↓                 ↓                     ↓
      formulario_socio  formulario_modificar   confirmación
         (CREATE)         (MODIFY) ← TÚ            (DELETE)
              │                  │                   │
              └──────────────────┴───────────────────┘
                        Guardar en NegocioSocio
                              ↓
                    Validar reglas de negocio
                              ↓
                    Mostrar lista actualizada

═════════════════════════════════════════════════════════════════════════════

ARCHIVOS CREADOS:
═════════════════════════════════════════════════════════════════════════════

1. practico_07/forms.py                 → Formularios
2. practico_07/views.py                 → Vistas/Controladores
3. practico_07/urls.py                  → Rutas
4. practico_07/settings.py              → Config Django
5. practico_07/__init__.py              → Marca como paquete
6. practico_07/manage.py                → Entry point
7. practico_07/templates/base.html                     → Base template
8. practico_07/templates/lista_socios.html            → Lista
9. practico_07/templates/formulario_socio.html        → Crear
10. practico_07/templates/formulario_modificar.html   → Modificar (COMPLETAR)

═════════════════════════════════════════════════════════════════════════════
""")
