from personas import Personas
from settings import BD,CSV
from clase_csv import Clase_csv
from sql import Sql

#TODO: 
# 1.- un if para verificar que al guardar, los datos no se van repetir, al no tener id los datos, sería recomendable compararlos por nombre con un if
# 2.- verificar que el numbre dado en la funcion mostrar_fila_desd_bd_por_nombre() es un str

class Manejador():
    def __init__(self) -> None:
       self.__bdatos = Sql(BD)

    def create(self):
        create_table = '''CREATE TABLE personas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        sex TEXT NOT NULL,
                        age INTEGER);
                        '''
        self.__bdatos.create(create_table)
        return 'Tabla creada'

    def guardar(self):
        obj_para_guardar = Clase_csv(CSV)
        lista_values = obj_para_guardar.muestra_values(0)
        logitud_csv = obj_para_guardar.num_en_lista()
        for fila in range(logitud_csv):
            lista_values = obj_para_guardar.muestra_values(fila)

            id = None
            nombre = lista_values[0]
            sexo = lista_values[1]
            edad = lista_values[2]

            p = Personas(id,nombre, sexo, edad)

            self.__bdatos.insert(p)

    def mostrar_fila_desd_bd_por_nombre(self,nombre):
        return self.__bdatos.select_por_nombre(nombre)

    def mostrar_filas(self):
        return self.__bdatos.select('SELECT * FROM personas')
