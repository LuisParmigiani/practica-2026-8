"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from practico_05.ejercicio_01 import Base, Socio
from sqlalchemy import select, insert, update, delete
from typing import List, Optional


class DatosSocio():

    def __init__(self):
        self.engine = create_engine("sqlite+pysqlite:///:memory:", echo=False)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.sesion = Session()

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        return self.sesion.query(Socio).filter(Socio.id == id_socio).first()

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        return self.sesion.query(Socio).filter(Socio.dni == dni_socio).first()

    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        return list(self.sesion.query(Socio).all())

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        result = self.sesion.query(Socio).delete()
        self.sesion.commit()
        if result > 0:
            return True
        return False

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        self.sesion.add(socio)
        self.sesion.commit()
        self.sesion.refresh(socio)  # Le pone el id generado
        return socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        socio = self.buscar(id_socio)
        if socio is None:
            return False
        self.sesion.delete(socio)
        self.sesion.commit()
        return True

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        stmt = update(Socio).where(Socio.id == socio.id).values(
            nombre=socio.nombre,
            apellido=socio.apellido,
            dni=socio.dni
        )
        self.sesion.execute(stmt)
        self.sesion.commit()
        return socio

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        return len(self.sesion.query(Socio).all())


# NO MODIFICAR - INICIO
# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587
assert len(datos.todos()) == 3
# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN
