import sqlite3

#TODO: Error en los nombres qaue tengan comilla como O'Dwyer(28), covertir consulta si tiene (\'O\'Dwyer) en una comilla u omitirla 
# y O'Driscoll(48) tambien tendrá ese problema 

class Sql():
    __cnx = None
    def __init__(self,bd) -> None:
        self.__bd = bd
    
    def conectar(self):
        if self.__cnx is None:
            self.__cnx = sqlite3.connect(self.__bd)
        return self.__cnx

    def insert(self, articulo):
        cnx = self.conectar()
        cur= cnx.cursor()
        consulta = self.prepara_insert(articulo)
        cur.execute(consulta) #'insert into personas(name,age,sex) values (\'O\'Dwyer, Miss. Ellen "Nellie"\',\'\',\'female\');'
        new_id = cur.lastrowid
        cnx.commit()
        return new_id
    
    def select(self, consulta):
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        filas = cur.fetchall()
        return filas

    def select_por_nombre(self, nombre):
        cnx = self.conectar()
        cur = cnx.cursor()
        nombre_minusculas = nombre.lower()
        consulta = f'SELECT name,sex,age FROM personas WHERE name like "%{nombre_minusculas}%"'
        cur.execute(consulta)
        filas = cur.fetchall()
        return filas

    def delete(self,articulo):
        tabla = type(articulo).__name__.lower()
        consulta = f'delete from {tabla} where id="{articulo.id}"'
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        cnx.commit()

    def prepara_insert(self,articulo):
        tabla = type(articulo).__name__.lower()
        campos = tuple(vars(articulo).keys())
        datos = vars(articulo)
        valores = ''
        campos = ''
        for k,v in datos.items():
            if k != 'id':
                valores += f"'{str(v)}',"
                campos += f'{k},'
        consulta = f"insert into {tabla}({campos[:-1]}) values ({valores[:-1]});"
        return consulta
        
    def create(self, consulta):#por probar
        cnx = self.conectar()
        cur = cnx.cursor()
        cur.execute(consulta)
        cnx.commit()
