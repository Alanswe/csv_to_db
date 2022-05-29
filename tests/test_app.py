import unittest
from app import Manejador

class Test_manejador(unittest.TestCase):
    def test_existencia(self):
        obj = Manejador()
        self.assertIsNotNone(obj)

    def test_buscar_por_nombre(self):
        obj = Manejador()
        busqueda = obj.mostrar_fila_desd_bd_por_nombre('celotti')
        self.assertEqual(busqueda,[('Celotti, Mr. Francesco', 'male', 24)])

    def test_muestra_filas(self):
        obj = Manejador()
        muestreo = obj.mostrar_filas()
        self.assertIsNotNone(muestreo)
        