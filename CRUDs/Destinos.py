from data import referenciaDestinos, Destinos

def getNewIdDestino():
    if len(Destinos) == 0:
        return 1
    return max_id_recursivo(Destinos) + 1

def max_id_recursivo(lista, indice=0, maximo=None):
    if indice == len(lista):
        return maximo
    
    if maximo is None or lista[indice][0] > maximo:
        maximo = lista[indice][0]
        return max_id_recursivo(lista, indice + 1, maximo)
# CREATE
def registrar_destino():
    print("\n--- Registro de Destino ---")
    nuevo = []
    nuevo_id = getNewIdDestino()
    nuevo.append(nuevo_id)

    destino = input("Ingrese nombre del destino: ")
 
    repetido = False
    for d in Destinos:
        if d[1] == destino:
            repetido = True
    if repetido:
        print("Ese destino ya existe.")
        return None
    nuevo.append(destino)

    descripcion = input("Ingrese la descripción: ")
    nuevo.append(descripcion)

    Destinos.append(nuevo)
    print("Destino registrado con ID:", nuevo_id)
    return nuevo_id

# READ
def mostrar_destinos():
    print("\n--- Lista de Destinos ---")
    print("ID | Destino | Descripción")
    for d in Destinos:
        print(d[0], "-", d[1], "-", d[2])

def buscar_destino():
    criterio = input("Ingrese destino a buscar: ")
    encontrados = []
    for d in Destinos:
        if criterio in d[1]:
            encontrados.append(d)
    if len(encontrados) > 0:
        print("\nResultados:")
        for d in encontrados:
            print("ID:", d[0], "-", d[1], "-", d[2])
    else:
        print("No se encontraron coincidencias.")

# UPDATE
def actualizar_destino():
    mostrar_destinos()
    try:
        did = int(input("Ingrese ID del destino a actualizar: "))
        for d in Destinos:
            if d[0] == did:
                print("Destino actual:", d[1], "-", d[2])
                nuevo_nombre = input("Nuevo nombre destino (Enter para mantener): ")
                if nuevo_nombre != "":
                    d[1] = nuevo_nombre
                nueva_desc = input("Nueva descripción (Enter para mantener): ")
                if nueva_desc != "":
                    d[2] = nueva_desc
                print("Destino actualizado.")
                return did
        print("No se encontró destino con ese ID.")
    except ValueError:
        print("ID inválido.")
    return None

# DELETE
def eliminar_destino():
    mostrar_destinos()
    try:
        did = int(input("Ingrese ID del destino a eliminar: "))
        for d in Destinos:
            if d[0] == did:
                Destinos.remove(d)
                print("Destino eliminado.")
                return did
        print("No se encontró destino con ese ID.")
    except ValueError:
        print("ID inválido.")
    return None

# MENU
def menu_destinos():
    salir = False
    while not salir:
        print()
        print("="*50)
        print("\n--- Menú Destinos ---")
        print("="*50)
        print("1. Registrar destino")
        print("2. Mostrar destinos")
        print("3. Buscar destino")
        print("4. Actualizar destino")
        print("5. Eliminar destino")
        print("0. Salir")
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
            print("Volviendo al menú...")
            print()
            salir = True
        else:
            print("⚠️ Opción inválida.")
