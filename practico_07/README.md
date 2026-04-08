# TP7 - Capa de Presentación: Gestión de Socios con Django

## 📋 Descripción

Esta es una aplicación Django que implementa la capa de presentación para gestionar Socios, utilizando la capa de negocio creada en `practico_06`.

## 🏗️ Estructura del Proyecto

```
practico_07/
├── forms.py                    # Formularios de Django
├── views.py                    # Vistas (lógica de presentación)
├── urls.py                     # Rutas de la aplicación
├── settings.py                 # Configuración de Django
├── __init__.py                 # Marca como paquete Python
├── templates/
│   ├── base.html               # Template base (herencia)
│   ├── lista_socios.html       # Lista de socios
│   ├── formulario_socio.html   # Formulario para crear
│   └── formulario_modificar.html # Formulario para modificar (¡DEBES COMPLETAR ESTO!)
└── manage.py                   # Punto de entrada
```

## 🎯 Requisitos

- Python 3.8+
- Django 4.0+
- SQLAlchemy (para los modelos)

## 🚀 Instalación y Ejecución

### 1. Instalar Django
```bash
pip install django
```

### 2. Estructura esperada del proyecto
Asegúrate que tu proyecto tenga esta estructura:
```
practica-2026-8/
├── practico_05/
│   └── ejercicio_01.py (contiene clase Socio)
├── practico_06/
│   └── capa_negocio.py (contiene NegocioSocio)
└── practico_07/ (esta carpeta)
```

### 3. Ejecutar el servidor Django
```bash
cd /Users/agus/Developer/practica-2026-8
python manage.py runserver
```

Luego abre en to navegador: `http://localhost:8000/socios/`

## 📚 Explicación del Código

### 1. **views.py** - Las vistas (Controladores)
Son funciones que manejan las peticiones HTTP:
- `lista_socios()` - GET /socios/ → Muestra tabla con todos los socios
- `crear_socio()` - GET/POST /socios/crear/ → Formulario para crear
- `modificar_socio()` - GET/POST /socios/modificar/<id>/ → Formulario para editar
- `eliminar_socio()` - POST /socios/eliminar/<id>/ → Elimina el socio

### 2. **forms.py** - Formularios Django
Define los campos y validaciones de cada formulario. Django automáticamente:
- Genera HTML del formulario
- Valida los datos
- Muestra errores

### 3. **templates/** - Presentación (HTML)
- `base.html` - Template base con navegación y estilos
- `lista_socios.html` - Tabla de socios, botones Alta/Baja/Modificar
- `formulario_socio.html` - Formulario para crear
- `formulario_modificar.html` - **✏️ TÚ DEBES COMPLETAR ESTO**

## ✏️ TU TAREA: Completar formulario_modificar.html

Debes completar el archivo `practico_07/templates/formulario_modificar.html`. Este template:

1. **Debe mostrar los mismos campos que `formulario_socio.html`**
2. **El campo DNI debe estar SOLO LECTURA** (no editable)
   - Usa: `readonly` attribute en el widget
3. **Los campos Nombre y Apellido deben ser editables**
4. **Botones:**
   - "Aceptar" (envía el POST)
   - "Cancelar" (vuelve a lista_socios)

### Guía para completarlo:

1. Abre [practico_07/templates/formulario_modificar.html](formulario_modificar.html)
2. Sigue el patrón de  [practico_07/templates/formulario_socio.html](formulario_socio.html)
3. **Diferencias clave:**
   - Agranda el DNI con `readonly` para que no se pueda cambiar
   - Reemplaza "Guardar" por "Aceptar"
   - Los tres campos (dni, nombre, apellido) están disponibles en el contexto

### Ejemplo de cómo hacer los campos readonly:

En `forms.py` ya está preparado para acepar una opción `attrs`. Pero en el template puedes también usar Django template logic.

---

## 🔧 Cómo funciona el flujo

### Alta de un socio:
1. Usuario hace click en "Alta" → Va a `/socios/crear/`
2. Django muestra `formulario_socio.html`
3. Usuario llena datos y hace click "Guardar"
4. POST para `/socios/crear/`
5. `crear_socio()` valida y llama a `negocio.alta(socio)`
6. Si falla = muestra error, si ok = redirige a lista

### Modificación de un socio:
1. Usuario hace click en "Modificar" en una fila → Va a `/socios/modificar/3/`
2. Django muestra `formulario_modificar.html` (¡que tú debes completar!)
3. Pre-rellena con datos actuales
4. Usuario edita nombre/apellido
5. Usuario hace click "Aceptar"
6. POST para `/socios/modificar/3/`
7. `modificar_socio()` valida y llama a `negocio.modificacion(socio)`
8. Si ok = redirige a lista

### Baja de un socio:
1. Usuario hace click en "Baja" → Envía POST a `/socios/eliminar/3/`
2. Django confirma con JavaScript (`onclick confirm()`)
3. `eliminar_socio()` llama a `negocio.baja(socio_id)`
4. Redirige lista

---

##  Próximos pasos

Una vez completes el formulario_modificar.html:

1. ✅ Prueba todas las operaciones:
   - ✅ Ver lista (está hecha)
   - ✅ Crear socio (está hecha)
   - ⚠️ Modificar socio (DEBES COMPLETAR TEMPLATE)
   - ✅ Eliminar socio (está hecha)

2. Verifica que los mensajes de error funcionen correctamente

3. Prueba casos de error:
   - DNI duplicado
   - Nombre/apellido < 3 caracteres
   - Nombre/apellido > 15 caracteres
   - Máximo de socios (200)

---

## 📝 Notas

- Los estilos usan Bootstrap 5 (CDN)
- Los mensajes se muestran usando Django Messages Framework
- El CSRF token está incluido en todos los formularios (seguridad)
- Los datos se guardan en memoria (usando la clase DatosSocio de practico_05)
