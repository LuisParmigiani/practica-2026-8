"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Socio

from typing import List, Optional

class DatosSocio():

    def __init__(self):
        self.engine = create_engine('sqlite:///socios.db') 
        # crea la tabla si es que no existe.
        Base.metadata.create_all(self.engine) 
        # crea las tablas definidas en el metadata (en este caso, la tabla 'socios' definida por la clase Socio)
        self.Session = sessionmaker(bind=self.engine, expire_on_commit=False) 
        # crea una clase Session que se puede usar para crear sesiones de conexión a la base de datos

        self.session = self.Session()
    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no 
        encuentra nada.
        """
        socio = self.session.query(Socio).filter(Socio.id_socio == id_socio).first() 
        return socio

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no 
        encuentra nada.
        """
        socio = self.session.query(Socio).filter(Socio.dni == dni_socio).first()
        return socio
        
    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        socios = self.session.query(Socio).all()
        return socios

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el 
        borrado fue exitoso.
        """
        try:
            self.session.query(Socio).delete()
            self.session.commit()
            return True
        except:
            return False

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        self.session.add(socio)
        self.session.commit()
        self.session.refresh(socio)
        return socio

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado 
        fue exitoso.
        """
        try:
            socio = self.session.query(Socio).filter(Socio.id_socio == id_socio).first()
            if socio:
                self.session.delete(socio)
                self.session.commit()
                return True
            return False
        except:
            return False

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio 
        modificado.
        """
        self.session.merge(socio)
        self.session.commit()
        return socio
    
    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        count = self.session.query(Socio).count()
        return count



# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()
print("Base de datos creada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0
print("Alta de socio realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Test Baja
assert datos.baja(socio.id_socio) == True
print("Baja de socio realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id_socio) == socio_2
print("Consulta de socio realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2  
print("Consulta de socio por DNI realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
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
print("Modificación de socio realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Test Conteo
assert len(datos.todos()) == 3
print("Conteo de socios realizada exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0
print("Borrado de todos los socios realizado exitosamente---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# NO MODIFICAR - FIN