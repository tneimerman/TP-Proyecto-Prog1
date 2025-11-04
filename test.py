from CRUDs.Archivos import * 
from data import referenciaPasajeros
from CRUDs.Pasajeros import *   
from CRUDs.Vuelos import mostrar_vuelos, get_destinos


archivo_modulo = "Archivos/Pasajeros.txt"

vuelo = ["6", "2", "1", "2026/12/02", "Directo"]

modificar_lista(archivo_modulo,"Juan",4, "1")
#guardar_data(vuelo, "Archivos/Vuelos.txt")
#lista = obtener_lista_por_id(6, "Archivos/Vuelos.txt")
#borrar_data("Archivos/Vuelos.txt", 6, lista)
#datos_pasajero(1)


