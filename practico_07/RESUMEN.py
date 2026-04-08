"""
RESUMEN: ¿QUÉ HACE CADA COMPONENTE?

Imagina que tu aplicación es un restaurante:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 forms.py = MENÚ
└─ Define qué campos pedirle al usuario (DNI, Nombre, Apellido)
└─ Valida que los datos sean correctos (nombre entre 3-15 caracteres)
└─ Si hay error, muestra un mensaje

🎮 views.py = COCINERO
├─ lista_socios()  → Compra y trae todos los socios a mostrar
├─ crear_socio()   → Recibe datos del formulario, valida, crea el socio
├─ modificar_socio()  → Recibe cambios, actualiza el socio
└─ eliminar_socio() → Borra el socio

🌐 urls.py = MAPA DE RUTAS
└─ Define dónde enviar cada petición:
   ├─ /socios/              → lista_socios()
   ├─ /socios/crear/        → crear_socio()
   ├─ /socios/modificar/3/  → modificar_socio(3)
   └─ /socios/eliminar/3/   → eliminar_socio(3)

🎨 templates/*.html = DISEÑO DEL RESTAURANTE
├─ base.html → La estructura general (decoraciones, barra de menú)
├─ lista_socios.html → La sala principal con la tabla de socios
├─ formulario_socio.html → El formulario para crear
└─ formulario_modificar.html → El formulario para editar (¡TÚ COMPLETAS!)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FLUJO DE UNA PETICIÓN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Usuario entra a http://localhost:8000/socios/
   ↓
2. Django ve en urls.py: "va a /socios/ → llama lista_socios()"
   ↓
3. lista_socios() obtiene todos los socios de NegocioSocio
   ↓
4. Renderiza lista_socios.html con esos socios
   ↓
5. El navegador muestra la tabla HTML

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CUANDO EL USUARIO HACE CLICK EN "MODIFICAR":
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Click en botón "Modificar" para socio ID=3
   ↓
2. Navega a http://localhost:8000/socios/modificar/3/
   ↓
3. Django ve: "va a /modificar/<id>/ → llama modificar_socio(3)"
   ↓
4. modificar_socio(3) busca el socio ID 3 en NegocioSocio
   ↓
5. Si es GET: Renderiza formulario_modificar.html PRELLENADO ← AQUÍ ESTÁS TÚ
   ↓
6. Si es POST: Valida datos y llama a negocio.modificacion(socio)
   ↓
7. Redirige a lista_socios para mostrar cambios

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

¿QUÉ SIGNIFICA PRELLENADO?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

En views.py ves this:

    form = SocioForm(initial={
        'dni': socio.dni,           # El campo DNI viene lleno
        'nombre': socio.nombre,     # El campo Nombre viene lleno
        'apellido': socio.apellido  # El campo Apellido viene lleno
    })

Esto significa que cuando el usuario abre el formulario, YA VE SUS DATOS.

En `formulario_modificar.html` debes mostrar ese formulario.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CÓMO COMPLETAR formulario_modificar.html:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Abre el archivo: practico_07/templates/formulario_modificar.html

2. Sigue el patrón de formulario_socio.html pero:
   
   ✅ COPIAR de formulario_socio.html:
      └─ La estructura HTML (form, divs, etc)
      └─ Los estilos de Bootstrap
      └─ La lógica de mostrar errores
   
   ❌ CAMBIAR:
      └─ El título de "Crear Socio" a "Modificar Socio"
      └─ El botón de texto de "Guardar" a "Aceptar"
      └─ El campo DNI debe tener "readonly" para NO poder editarlo
      └─ Agregar línea: <p class="text-muted">Socio ID: {{ socio.id }}</p>

3. Campos a incluir exactamente en este orden:
   
   a) Campo DNI       → {{ form.dni }}  + readonly
   b) Campo Nombre    → {{ form.nombre }}
   c) Campo Apellido  → {{ form.apellido }}
   
   Cada uno con:
   - <label> con el nombre del campo
   - El input del formulario
   - Div para mostrar errores si hay

4. Botones:
   - Botón Submit "Aceptar"
   - Link a lista_socios "Cancelar"

═════════════════════════════════════════════════════════════════════════════

DIFERENCIA ENTRE formulario_socio.html y formulario_modificar.html:
═════════════════════════════════════════════════════════════════════════════

                        formulario_socio     |  formulario_modificar
                        (CREATE - Alta)      |  (MODIFY - Modificar)
─────────────────────────────────────────────┼──────────────────────────────
Disponibles para editar:                      |
  DNI                     ✅ Editable         |     ❌ Readonly (no editar)
  Nombre                  ✅ Editable         |     ✅ Editable
  Apellido                ✅ Editable         |     ✅ Editable
                                              |
Botón submit             "Guardar"           |     "Aceptar"
                                              |
Mostrar ID socio         N/A (es nuevo)      |     Mostrar ID: {{ socio.id }}
                                              |
Punto de destino         POST /crear/        |     POST /modificar/{{ id }}/

═════════════════════════════════════════════════════════════════════════════

¿POR QUÉ EL DNI ES READONLY?
═════════════════════════════════════════════════════════════════════════════

Recuerda la "Regla 1" en NegocioSocio:
  
  def regla_1(self, socio):
      ""Validar que el DNI del socio es unico""
      
El DNI es ÚNICO. No puedes cambiar un DNI por otro que ya existe.
¿Qué pasaría si dejaras editar el DNI?

  ❌ Usuario 1: DNI=12345678  Nombre=Juan
  ❌ Usuario quiere cambiar DNI a 87654321
  ❌ ¡Pero ese DNI ya existe en otro socio!
  ❌ Violaría la regla 1

Por eso el DNI debe ser READONLY (solo lectura):

  <input ... readonly> ← No se puede editar pero se ve el valor

═════════════════════════════════════════════════════════════════════════════
"""

print(__doc__)
