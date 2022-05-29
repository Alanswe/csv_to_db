import unittest
from settings import CSV
from clase_csv import Clase_csv

class Test_opercaiones_csv(unittest.TestCase):
    def test_existencia(self):
        obj = Clase_csv(CSV)
        self.assertIsNotNone(obj)

    def test_return_csv(self):
        obj = Clase_csv(CSV)
        primera_columna = obj.leer_archivo()[0] # Elijo solo uno para agilizar el test
        self.assertEqual(primera_columna,{'Name': 'Braund, Mr. Owen Harris', 'Sex': 'male', 'Age': '22'})

    # def test_retun_lista_completa(self):
    #     obj = Clase_csv(CSV)
    #     lista_completa = obj.leer_archivo()
    #     self.assertListEqual(lista_completa,[]) #Demasiado lago ¿Como lo hago?

    def test_retun_keys(self):
        obj = Clase_csv(CSV)
        keys = obj.muestra_keys()
        self.assertEqual(keys,['Name', 'Sex', 'Age'])

    def test_retun_values(self):
        obj = Clase_csv(CSV)
        values = obj.muestra_values(0)
        self.assertEqual(values,['Braund, Mr. Owen Harris', 'male', '22'])

    def test_retun_value_primero(self):
        obj = Clase_csv(CSV)
        values = obj.muestra_values(0)[0]
        self.assertEqual(values,'Braund, Mr. Owen Harris')

    def test_retun_num_elementos_in_lista_completa(self):
        obj = Clase_csv(CSV)
        numero_de_filas = obj.num_en_lista()
        self.assertEqual(numero_de_filas,99)

    def test_retun_num_elementos_in_lista_completa_sin_llamada(self):
        obj = Clase_csv(CSV)
        lista_completa = len(obj.leer_archivo())
        self.assertEqual(lista_completa,99)
