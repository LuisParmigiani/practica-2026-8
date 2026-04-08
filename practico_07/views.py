# Vistas de Django para gestionar Socios

import os
from django.shortcuts import render, redirect
from django.contrib import messages
from practico_06.capa_negocio import NegocioSocio, DniRepetido, LongitudInvalida, MaximoAlcanzado
from practico_05.ejercicio_01 import Socio, Base
from practico_05.ejercicio_02 import DatosSocio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .forms import SocioForm


# Crear una versión modificada de DatosSocio con BD persistente
class DatosSocioPersistente(DatosSocio):
    def __init__(self):
        # Usar una BD SQLite persistente en lugar de in-memory
        db_path = os.path.join(os.path.dirname(__file__), 'socios.db')
        self.engine = create_engine(
            f"sqlite+pysqlite:///{db_path}", echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.sesion = Session()


# Crear una versión modificada de NegocioSocio que use la BD persistente
class NegocioSocioPersistente(NegocioSocio):
    def __init__(self):
        self.datos = DatosSocioPersistente()


# Instancia global de la capa de negocio con BD persistente
negocio = NegocioSocioPersistente()


def lista_socios(request):
    """
    Vista que muestra la lista de todos los socios en una tabla
    """
    socios = negocio.todos()
    return render(request, 'lista_socios.html', {'socios': socios})


def crear_socio(request):
    """
    Vista para crear un nuevo socio.
    GET: Muestra el formulario vacío
    POST: Procesa los datos y guarda el nuevo socio
    """
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            try:
                # Crear instancia de Socio con los datos del formulario
                socio = Socio(
                    dni=form.cleaned_data['dni'],
                    nombre=form.cleaned_data['nombre'],
                    apellido=form.cleaned_data['apellido']
                )

                # Intentar dar de alta
                negocio.alta(socio)
                messages.success(
                    request, f'Socio {socio.nombre} creado exitosamente.')
                return redirect('lista_socios')

            except DniRepetido:
                messages.error(request, 'Error: El DNI ya está registrado.')
            except LongitudInvalida:
                messages.error(
                    request, 'Error: Nombre y apellido deben tener entre 3 y 15 caracteres.')
            except MaximoAlcanzado:
                messages.error(
                    request, 'Error: Se alcanzó el máximo de socios permitidos.')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
    else:
        form = SocioForm()

    return render(request, 'formulario_socio.html', {'form': form, 'titulo': 'Crear Socio'})


def modificar_socio(request, socio_id):
    """
    Vista para modificar un socio existente.
    GET: Muestra el formulario con los datos actuales
    POST: Procesa los cambios y actualiza el socio
    """
    # Buscar el socio
    socio = negocio.buscar(socio_id)
    if not socio:
        messages.error(request, 'Socio no encontrado.')
        return redirect('lista_socios')

    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            try:
                # Actualizar datos del socio
                socio.nombre = form.cleaned_data['nombre']
                socio.apellido = form.cleaned_data['apellido']

                # Guardar cambios
                negocio.modificacion(socio)
                messages.success(request, 'Socio modificado exitosamente.')
                return redirect('lista_socios')

            except LongitudInvalida:
                messages.error(
                    request, 'Error: Nombre y apellido deben tener entre 3 y 15 caracteres.')
            except Exception as e:
                messages.error(request, f'Error al modificar: {str(e)}')
    else:
        # Prellenar el formulario con los datos actuales
        form = SocioForm(initial={
            'dni': socio.dni,
            'nombre': socio.nombre,
            'apellido': socio.apellido
        })

    return render(request, 'formulario_modificar.html', {
        'form': form,
        'socio': socio,
        'titulo': 'Modificar Socio'
    })


def eliminar_socio(request, socio_id):
    """
    Vista para eliminar un socio.
    Solo procesa POST (para seguridad)
    """
    socio = negocio.buscar(socio_id)
    if not socio:
        messages.error(request, 'Socio no encontrado.')
        return redirect('lista_socios')

    if request.method == 'POST':
        nombre_socio = f"{socio.nombre} {socio.apellido}"
        negocio.baja(socio_id)
        messages.success(
            request, f'Socio {nombre_socio} eliminado exitosamente.')
        return redirect('lista_socios')

    # Si no es POST, redirigir a la lista
    return redirect('lista_socios')
