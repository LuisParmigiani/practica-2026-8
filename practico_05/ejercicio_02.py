"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from practico_05.ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        engine = create_engine('sqlite:///:memory:', echo=True) #engine es el motor entre el ORM y la base SQLite
        #:memory: es una base en memoria que dura lo que dura el programa
        # el echo es para ver todas las consultas sql que se hacen a la base. bueno para debugging
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        return self.session.query(Socio).filter(Socio.id_socio == id_socio).first() 

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        return self.session.query(Socio).filter(Socio.dni == dni_socio).first() 

    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        return self.session.query(Socio).all()

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        self.session.query(Socio).delete() #Si quisiera borrar un solo socio, haria un filter(Socio.id_socio == id_socio).delete()
        self.session.commit()
        return True

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        self.session.add(socio)
        self.session.commit()
        return socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        #socio_a_borrar = self.buscar(id_socio)
        #if socio_a_borrar:
        #    self.session.delete(socio_a_borrar)
        #    self.session.commit()
        #    return True
        #return False ESTO ES REUTILIZANDO EL MÉTODO Y PASANDO EL OBJETO

        if self.session.query(Socio).filter(Socio.id_socio == id_socio).delete(): #ESTO ES HACIENDO TODO EN UNA SOLA CONSULTA, SIN REUTILIZAR EL MÉTODO DE BUSCAR
            self.session.commit()
            return True
        return False
    

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        self.session.add(socio)
        self.session.commit()
        return socio

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        return self.session.query(Socio).count() #Mas eficiente
        #return len(self.todos()) Menos eficiente, porque hace una consulta para traer todos los socios
        #  y luego cuenta la cantidad de objetos


# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id_socio) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id_socio)
assert socio_3_modificado.id_socio == socio_3.id_socio
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN