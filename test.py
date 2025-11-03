from CRUDs.Archivos import * 
from data import referenciaPasajeros
from CRUDs.Pasajeros import *   
from CRUDs.Vuelos import mostrar_vuelos, get_destinos


archivo_modulo = "Archivos/Vuelos.txt"

aero = ["5", "Air France", "Boeing 777"]

#save_data(aero, "Archivos/Aerolinea.txt")
#delete_data("Archivos/Aerolinea.txt", 6)
#datos_pasajero(1)
#mostrar_vuelos()

id = get_destinos()