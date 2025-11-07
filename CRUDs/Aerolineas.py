from referencias import referenciaAerolinea
from Helpers.Archivos import *

ARCHIVO_AEROLINEAS = "Archivos/Aerolineas.txt"


def max_id_recursivo(lista, indice=0, maximo=None):
    if indice == len(lista):
        return int(maximo) if maximo is not None else 0
    actual = int(lista[indice][0])
    if maximo is None or actual > maximo:
        maximo = actual
    return max_id_recursivo(lista, indice + 1, maximo)

def getNewIdAerolinea():
    lista = obtener_matriz(ARCHIVO_AEROLINEAS)
    if lista is None or len(lista) == 0:
        return 1
    return max_id_recursivo(lista) + 1

# CREATE
def registrar_aerolinea():
    print("\n--- Registro de Aerolínea ---")
    nuevo_id = getNewIdAerolinea()
    nombre = input("Ingrese nombre de la aerolínea: ")

    lista = obtener_matriz(ARCHIVO_AEROLINEAS)
    for a in lista:
        if a[1] == nombre:
            print("Esa aerolínea ya existe.")
            return

    modelo = input("Ingrese el modelo del avión: ")
    nuevo = [nuevo_id, nombre, modelo]
    guardar_data(ARCHIVO_AEROLINEAS, nuevo)
    print("Aerolínea registrada con ID:", nuevo_id)

# READ
def mostrar_aerolineas():
    print("\n--- Lista de Aerolíneas ---")
    print("║ID║      Nombre      ║      Modelo      ║")
    mostrar_informacion(ARCHIVO_AEROLINEAS)

def buscar_aerolineas():
    print("\n--- Buscar Aerolíneas ---")
    print("1. Mostrar todas")
    print("2. Buscar por ID")
    print("3. Buscar por nombre")
    print("4. Buscar por modelo")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_aerolineas()
    elif opcion == "2":
        aid = input("Ingrese el ID: ")
        resultado = obtener_lista_por_id(aid, ARCHIVO_AEROLINEAS)
        if resultado:
            print("Resultado encontrado:", resultado)
        else:
            print("No se encontró la aerolínea.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre: ")
        resultado = obtener_lista_por_dato(nombre, ARCHIVO_AEROLINEAS)
        if resultado:
            print("Resultado encontrado:", resultado)
        else:
            print("No se encontró la aerolínea.")
    elif opcion == "4":
        modelo = input("Ingrese el modelo: ")
        resultado = obtener_lista_por_dato(modelo, ARCHIVO_AEROLINEAS)
        if resultado:
            print("Resultado encontrado:", resultado)
        else:
            print("No se encontró la aerolínea.")
    else:
        print("Opción inválida.")

# UPDATE
def actualizar_aerolinea():
    mostrar_aerolineas()
    aid = input("Ingrese el ID de la aerolínea a actualizar: ")
    print("1. Modificar nombre")
    print("2. Modificar modelo")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo = input("Ingrese el nuevo nombre: ")
        modificar_lista(ARCHIVO_AEROLINEAS, nuevo, 1, aid)
    elif opcion == "2":
        nuevo = input("Ingrese el nuevo modelo: ")
        modificar_lista(ARCHIVO_AEROLINEAS, nuevo, 2, aid)
    else:
        print("Opción inválida.")

# DELETE
def eliminar_aerolinea():
    mostrar_aerolineas()
    aid = input("Ingrese el ID de la aerolínea a eliminar: ")
    lista = obtener_lista_por_id(aid, ARCHIVO_AEROLINEAS)
    if lista:
        borrar_data(ARCHIVO_AEROLINEAS, aid, lista)
    else:
        print("No se encontró la aerolínea con ese ID.")

# MENU
def menu_aerolineas():
    salir = False
    while not salir:
        print()
        print("="*50)
        print("--- Menú Gestión de Aerolíneas ---")
        print("="*50)
        print("1. Registrar nueva aerolínea")
        print("2. Buscar aerolíneas")
        print("3. Actualizar aerolínea")
        print("4. Eliminar aerolínea")
        print("0. Salir")
        print("="*50)
        op = input("Seleccione una opción: ")

        if op == "1":
            registrar_aerolinea()
        elif op == "2":
            buscar_aerolineas()
        elif op == "3":
            actualizar_aerolinea()
        elif op == "4":
            eliminar_aerolinea()
        elif op == "0":
            salir = True
        else:
            print("⚠️ Opción inválida.")
