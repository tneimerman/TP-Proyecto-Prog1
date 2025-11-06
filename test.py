from Helpers.Archivos import * 
from referencias import *
from CRUDs.Pasajeros import *   
from CRUDs.Vuelos import mostrar_vuelos, get_destinos
from Helpers.JSON import *
from CRUDs.VueloPasajero import *

archivo_modulo = "Archivos/Pasajeros.txt"

vuelo = ["6", "2", "1", "2026/12/02", "Directo"]
dic1 = {"ID": 5, "IdPasajero": 4, "IdVuelo": 3}
#modificar_lista(archivo_modulo,"Juan",4, "1")
#guardar_data(vuelo, "Archivos/Vuelos.txt")
#lista = obtener_lista_por_id(6, "Archivos/Vuelos.txt")
#borrar_data("Archivos/Vuelos.txt", 6, lista)
#datos_pasajero(1)
#guardar_diccionario(dic1)
#eliminar_diccionario(5)
#dict = modificar_diccionario(3, "IdVuelo", 1)
dict = obtener_diccionarios()
print(dict)
verificar_relacion_existente(2, "IdVuelo", dict)