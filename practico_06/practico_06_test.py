# Implementar los casos de prueba descriptos.

import unittest

from practico_05.ejercicio_01 import Socio
from practico_06.capa_negocio import DniRepetido, MaximoAlcanzado, NegocioSocio, LongitudInvalida


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp() #Antes de cada test, se ejecuta el setUp que crea la instancia NegocioSocio
        self.ns = NegocioSocio() #los argumentos de super son innecesarios en py3, dice dame la base de TestNegocio con este self

    def tearDown(self):
        super(TestsNegocio, self).tearDown() #Después de cada test, se ejecuta el tearDown que borra todos los socios
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
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)

        # valida regla
        valido = Socio(dni=12345679, nombre='Carlos', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        # dni repetido
        invalido = Socio(dni=12345678, nombre='Carlos', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)


    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='JuanPerezJuanPerez', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='PerezPerezPerezPerez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):
        # valida regla
        for i in range((self.ns.MAX_SOCIOS)-1):
            socio = Socio(dni=12345678 + i, nombre='Juan', apellido='Perez')
            self.ns.alta(socio)
        self.assertTrue(self.ns.regla_3())

        # maximo alcanzado
        socio = Socio(dni=12345678 + self.ns.MAX_SOCIOS, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3)

    def test_baja(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.ns.alta(socio)
        self.assertTrue(self.ns.baja(socio))

    def test_buscar(self):
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        socio_encontrado = self.ns.buscar(socio.id_socio)
        self.assertEqual(socio, socio_encontrado)

    def test_buscar_dni(self):
        #Verificar assert
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
        socio_encontrado = self.ns.buscar_dni(socio.dni)
        self.assertEqual(socio, socio_encontrado)

        #Verificar que no encuentra un dni que no existe
        socio_encontrado = self.ns.buscar_dni(12345679)
        self.assertIsNone(socio_encontrado)

    def test_todos(self):
        #Comparamos solo la cantidad porque para comparar objetos hay que definir __eq__ o hacer una lista de atributos a comparar.
        listaSociosACargar = [
            Socio(dni=12345678, nombre='Juan', apellido='Perez'),
            Socio(dni=12345679, nombre='Carlos', apellido='Perez'),
            Socio(dni=12345680, nombre='Susana', apellido='Gimenez')
        ]
        for socio in listaSociosACargar:
            self.ns.alta(socio)
        listaSocios = self.ns.todos()
        self.assertEqual(len(listaSocios), len(listaSociosACargar))

    def test_modificacion(self):
        # validamos longitudes mínimas, no max pq deberían cumplirse tmb
        socio = Socio(dni=12345678, nombre='Ju', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.modificacion, socio)

        socio = Socio(dni=12345678, nombre='Juan', apellido='Pe')
        self.assertRaises(LongitudInvalida, self.ns.modificacion, socio)

        # ingresamos un socio válido
        socio = self.ns.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))

        # validamos que no se pueda modificar a un dni repetido
        socio_2 = Socio(dni=12345678, nombre='Carlos', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.modificacion, socio_2)

        # validamos que se pueda modificar el nombre y apellido
        socio.nombre = 'Moria'
        socio.apellido = 'Casan'
        self.assertTrue(self.ns.modificacion(socio))
        socio_modificado = self.ns.buscar(socio.id_socio)
        self.assertEqual(socio_modificado.nombre, 'Moria')
        self.assertEqual(socio_modificado.apellido, 'Casan')    

