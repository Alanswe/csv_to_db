import unittest
from settings import CSV, CSV_original

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
    
    # Extras con el csv titanic original -----------

    def test_retun_keys_de_titanic_csv_original(self):
        obj = Clase_csv(CSV_original)
        keys = obj.muestra_keys()
        self.assertEqual(keys,['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'])

    def test_muestra_lista_de_diccinarios(self):
        obj = Clase_csv(CSV_original)
        muestreo = obj.leer_archivo()
        self.assertIsNotNone(muestreo)

    def test_retun_value_primero_de_titanic_csv_original(self):
        obj = Clase_csv(CSV_original)
        values = obj.muestra_values(0)
        self.assertEqual(str(values),"['1', '0', '3', 'Braund, Mr. Owen Harris', 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']") # Se paso a STR por la siguiente razón:
        # Ticket 'A/5 21171 lo determina como [52 chars] -> AssertionError: ['1', '0', '3', 'Braund, Mr. Owen Harris[52 chars]'S']

    def test_retun_value_primero_de_titanic_csv_original_con_lista_completa(self):
        obj = Clase_csv(CSV_original)
        muestreo = obj.leer_archivo()[0]
        self.assertEqual(muestreo,{'PassengerId': '1', 'Survived': '0', 'Pclass': '3', 'Name': 'Braund, Mr. Owen Harris', 'Sex': 'male', 'Age': '22', 'SibSp': '1', 'Parch': '0', 'Ticket': 'A/5 21171', 'Fare': '7.25', 'Cabin': '', 'Embarked': 'S'})
        