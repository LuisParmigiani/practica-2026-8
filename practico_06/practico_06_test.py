# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        # primer socio con DNI 12345678 - debe pasar
        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(socio1))

        # segundo socio con mismo DNI - debe fallar
        socio2 = Socio(dni=12345678, nombre='Carlos', apellido='Lopez')
        self.ns.alta(socio1)
        self.assertRaises(DniRepetido, self.ns.regla_1, socio2)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='J' * 16, apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P' * 16)
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # agregar socios hasta alcanzar el maximo
        for i in range(self.ns.MAX_SOCIOS):
            socio = Socio(dni=1000000 + i, nombre='Juan', apellido='Perez')
            self.ns.alta(socio)

        # intentar agregar uno mas - debe fallar
        socio_extra = Socio(dni=9999999, nombre='Carlos', apellido='Lopez')
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        # agregar un socio
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio_agregado = self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)

        # eliminar el socio
        exito = self.ns.baja(socio_agregado.id)
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        # agregar un socio
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio_agregado = self.ns.alta(socio)

        # buscar por id
        encontrado = self.ns.buscar(socio_agregado.id)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.dni, 12345678)

        # buscar id inexistente
        no_encontrado = self.ns.buscar(9999)
        self.assertIsNone(no_encontrado)

    def test_buscar_dni(self):
        # agregar un socio
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # buscar por dni
        encontrado = self.ns.buscar_dni(12345678)
        self.assertIsNotNone(encontrado)
        self.assertEqual(encontrado.nombre, 'Juan')

        # buscar dni inexistente
        no_encontrado = self.ns.buscar_dni(9999999)
        self.assertIsNone(no_encontrado)

    def test_todos(self):
        # inicialmente sin socios
        self.assertEqual(len(self.ns.todos()), 0)

        # agregar varios socios
        socio1 = Socio(dni=11111111, nombre='Juan', apellido='Perez')
        socio2 = Socio(dni=22222222, nombre='Carlos', apellido='Lopez')
        socio3 = Socio(dni=33333333, nombre='Maria', apellido='Garcia')

        self.ns.alta(socio1)
        self.ns.alta(socio2)
        self.ns.alta(socio3)

        # verificar que devuelve los 3
        todos = self.ns.todos()
        self.assertEqual(len(todos), 3)

    def test_modificacion(self):
        # agregar un socio
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        socio_agregado = self.ns.alta(socio)

        # modificar datos validos
        socio_agregado.nombre = 'Carlos'
        socio_agregado.apellido = 'Lopez'
        exito = self.ns.modificacion(socio_agregado)
        self.assertTrue(exito)

        # verificar cambios
        modificado = self.ns.buscar(socio_agregado.id)
        self.assertEqual(modificado.nombre, 'Carlos')
        self.assertEqual(modificado.apellido, 'Lopez')
