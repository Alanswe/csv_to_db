import csv

class Clase_csv():
    def __init__(self,archivo_csv) -> None:
        self.__csv = archivo_csv
        # self.__obj = Clase_csv(CSV) # esto me ayudaria a quitar código repetido pero me da error RecursionError: maximum recursion depth exceeded

    def leer_archivo(self):
        csv_in = open(self.__csv) 
        lector_dic = csv.DictReader(csv_in)
        lista_dict = list(lector_dic)
        csv_in.close()
        return lista_dict

    def muestra_keys(self):
        """
        Partiendo de la primera columna de datos, muestra las claves y las devuelve en una lista.
        """
        obj_for_keys = Clase_csv(self.__csv)
        dicci = obj_for_keys.leer_archivo()[0]
        keys = list(dicci.keys())
        return keys

    def muestra_values(self,num_fila):
        """
        Dado un numero de fila dado, crea un objeto de un objeto especial para esta funcion,
        del que saca un diccionario del numero de fila dado para extraer los valores y 
        devolverlos en foma de lista.
        """
        obj_for_values = Clase_csv(self.__csv)
        dicci = obj_for_values.leer_archivo()[num_fila]
        values = list(dicci.values())
        return values

    def num_en_lista(self):
        obj_for_count = Clase_csv(self.__csv)
        numero_de_filas = len(obj_for_count.leer_archivo())
        return numero_de_filas
