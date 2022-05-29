from app import Manejador
import platform
import os
from pprint import pprint
objeto = Manejador()


my_os = platform.system()

if my_os == 'Windows':
    limpiar_pantalla = os.system('cls')
else:
    limpiar_pantalla = os.system('clear')

limpiar_pantalla

# ---------- Mensajes y menús ----------
menu = """¿Que desea hacer?
1 - Guardar csv en Base de Datos (Después de una vez ejecutada, guarda repetidos cada vez que se ejecute esta opción)
2 - Mostrar fila por nombre
3 - Mostrar csv completo
"""
nombre_para_busqueda = """¿Que nombre buscamos? """
mensaje_exit = """Hasta luego lucarr"""
# ---------- ----------


encabezado = input(menu)

if encabezado == '1':
    limpiar_pantalla
    objeto.guardar()
    print('Ea po ya está guardao')
elif encabezado == '2':
    limpiar_pantalla
    nombre = input(nombre_para_busqueda)
    pprint(objeto.mostrar_fila_desd_bd_por_nombre(nombre))
elif encabezado == '3':
    limpiar_pantalla
    pprint(objeto.mostrar_filas())
else:
    limpiar_pantalla
    print(mensaje_exit) # preguntar a Teo lo de volver a la linea 11 (en este caso)
    