"""Base de Datos SQL - Búsqueda"""

import datetime
import sqlite3

from practico_04.ejercicio_01 import reset_tabla
from practico_04.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una 
    persona basado en su id. El return es una tupla que contiene sus campos: 
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro, 
    devuelve False."""
    conn = sqlite3.connect("practico_04/ejercicio_01.db")
    cursor = conn.cursor()
    result = cursor.execute('''
                select * from Persona where IdPersona = ?
''', (id_persona,))
    person = result.fetchone()
    if person is None:
        return False
    # Lo paso a datetime xq sino va a tirar error en la comparacion, de sqlite viene en string xq no lo soporta
    person = list(person)
    person[2] = datetime.datetime.strptime(person[2], "%Y-%m-%d")
    return tuple(person)


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona(
        'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(
        1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False


if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN
