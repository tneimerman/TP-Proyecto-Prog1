from CRUDs.Archivos import * 
from data import referenciaPasajeros
from CRUDs.Pasajeros import *   
from CRUDs.Vuelos import mostrar_vuelos, get_destinos


archivo_modulo = "Archivos/Vuelos.txt"

vuelo = ["6", "2", "1", "2026/12/02", "Directo"]

#save_data(vuelo, "Archivos/Vuelos.txt")
lista = get_lista_by_id(6, "Archivos/Vuelos.txt")
delete_data("Archivos/Vuelos.txt", 6, lista)
#datos_pasajero(1)


