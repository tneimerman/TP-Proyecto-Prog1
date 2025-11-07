from referencias import referenciaDestinos
from Helpers.Archivos import *

ARCHIVO_DESTINOS = "Archivos/Destinos.txt"

def max_id_recursivo(lista, indice=0, maximo=None):
    if indice == len(lista):
        return int(maximo) if maximo is not None else 0
    actual = int(lista[indice][0])
    if maximo is None or actual > maximo:
        maximo = actual
    return max_id_recursivo(lista, indice + 1, maximo)

def getNewIdDestino():
    lista = obtener_matriz(ARCHIVO_DESTINOS)
    if lista is None or len(lista) == 0:
        return 1
    return max_id_recursivo(lista) + 1

# CREATE
def registrar_destino():
    print("\n--- Registro de Destino ---")
    nuevo_id = getNewIdDestino()
    destino = input("Ingrese nombre del destino: ")

    lista = obtener_matriz(ARCHIVO_DESTINOS)
    for d in lista:
        if d[1] == destino:
            print("Ese destino ya existe.")
            return

    descripcion = input("Ingrese la descripción: ")
    nuevo = [nuevo_id, destino, descripcion]
    guardar_data(ARCHIVO_DESTINOS, nuevo)
    print("Destino registrado con ID:", nuevo_id)

# READ
def mostrar_destinos():
    print("\n--- Lista de Destinos ---")
    print("║ID║     Destino     ║   Descripción   ║")
    mostrar_informacion(ARCHIVO_DESTINOS)

def buscar_destino():
    print("\n--- Buscar Destino ---")
    print("1. Mostrar todos")
    print("2. Buscar por ID")
    print("3. Buscar por nombre")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_destinos()
    elif opcion == "2":
        did = input("Ingrese el ID: ")
        resultado = obtener_lista_por_id(did, ARCHIVO_DESTINOS)
        if resultado:
            print("Resultado encontrado:", resultado)
        else:
            print("No se encontró el destino.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre del destino: ")
        resultado = obtener_lista_por_dato(nombre, ARCHIVO_DESTINOS)
        if resultado:
            print("Resultado encontrado:", resultado)
        else:
            print("No se encontró el destino.")
    else:
        print("Opción inválida.")

# UPDATE
def actualizar_destino():
    mostrar_destinos()
    did = input("Ingrese el ID del destino a actualizar: ")
    print("1. Modificar nombre")
    print("2. Modificar descripción")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nuevo = input("Ingrese el nuevo nombre: ")
        modificar_lista(ARCHIVO_DESTINOS, nuevo, 1, did)
    elif opcion == "2":
        nuevo = input("Ingrese la nueva descripción: ")
        modificar_lista(ARCHIVO_DESTINOS, nuevo, 2, did)
    else:
        print("Opción inválida.")

# DELETE
def eliminar_destino():
    mostrar_destinos()
    did = input("Ingrese el ID del destino a eliminar: ")
    lista = obtener_lista_por_id(did, ARCHIVO_DESTINOS)
    if lista:
        borrar_data(ARCHIVO_DESTINOS, did, lista)
    else:
        print("No se encontró el destino con ese ID.")

# MENU
def menu_destinos():
    salir = False
    while not salir:
        print()
        print("="*50)
        print("--- Menú de Destinos ---")
        print("="*50)
        print("1. Registrar destino")
        print("2. Mostrar destinos")
        print("3. Buscar destino")
        print("4. Actualizar destino")
        print("5. Eliminar destino")
        print("0. Volver")
        print("="*50)
        op = input("Opción: ")

        if op == "1":
            registrar_destino()
        elif op == "2":
            mostrar_destinos()
        elif op == "3":
            buscar_destino()
        elif op == "4":
            actualizar_destino()
        elif op == "5":
            eliminar_destino()
        elif op == "0":
            salir = True
        else:
            print("⚠️ Opción inválida.")
