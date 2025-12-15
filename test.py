from Helpers import *
from CRUDs import *
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
#dict = obtener_diccionarios()
#print(dict)
#verificar_relacion_existente(2, "IdVuelo", dict)
#v,d = verificar_dias("02", "30", "2001")
#v,m = verificar_mes("14")
#print(d)
#print(m)
#validar_fecha("2025/02/29")
#test_validar_mail()
#getNewIdAerolinea()
#lista = fix_info("1;12345;jperez@gmail.com;40123456;Juan;Perez;1134567890;1990/05/14")
#print(lista)
#guardar_usuario(lista)
lista = obtener_lista_por_dato("anamartinez@yahoo.com.ar",archivo_modulo)
#lista = obtener_lista_por_id(6,archivo_modulo)
print(lista)