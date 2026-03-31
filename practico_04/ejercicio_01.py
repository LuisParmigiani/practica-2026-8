"""Base de Datos SQL - Crear y Borrar Tablas"""

import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (autoincremental)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    conn = sqlite3.connect('ejercicio_01.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Persona (
            IdPersona INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR(30),
            FechaNacimiento DATE,
            DNI INTEGER,
            Altura INTEGER
        )
    ''')
    conn.commit()
    conn.close()


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    conn = sqlite3.connect('ejercicio_01.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Persona')
    conn.commit()
    conn.close()

# ANDA, LO PROBÉ EJECUTANDO UN PAR SI EL ARCHIVO TENÍA POR NOMBRE MAIN (CORRER EN MODO SCRIPT) Y FUNCIONA.

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN
