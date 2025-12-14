from referencias import referenciaVuelos, referenciaDestinos,referenciaAerolinea
from CRUDs.Destinos import mostrar_destinos 
from Helpers import validar_fecha
from Helpers.Archivos import *
archivo_modulo = "Archivos/Vuelos.txt"

def max_id_recursivo(count, indice=0, maximo=None):
    if indice == len(count):
        return int(maximo) if maximo is not None else 0
    id = obtener_lista_por_id(indice+1,archivo_modulo)
    actual = int(id[0])
    if maximo is None or actual > maximo:
        maximo = actual
    return max_id_recursivo(count, indice + 1, maximo)

def existe_referencia_recursiva(lista, ref, indice=0):
    if indice == len(lista): 
        return False
    if str(lista[indice][0]) == str(ref):
        return True
    return existe_referencia_recursiva(lista, ref, indice + 1)


def getNewId():
    count    = obtener_max_archivo(archivo_modulo)
    if count == 0:
        return 1
    return max_id_recursivo(count) + 1

def get_vuelos():

    try:
        arch = open(archivo_modulo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            lista[1] = obtener_lista_por_id(lista[1],"Archivos/Aerolinea.txt")
            lista[2] = obtener_lista_por_id(lista[2],"Archivos/Destinos.txt")
            for x in lista:
                print(f"║{x:^20}", end="")
            print()

    except OSError:
        print("No se pudo leer el archivo")

    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")


def get_vuelo_by_referencia(pos, ref):
    try:
        arch = open(archivo_modulo, "r", encoding="UTF-8")
        for linea in arch:
            x = fix_info(linea)
            if str(ref) == x[pos]:
                return x
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def get_fecha():
    while True:
        try:
            fecha = input("Ingrese fecha de llegada (AAAA/MM/DD): ")
            validar_fecha(fecha)
            return fecha
        except ValueError:
            print("Fecha invalida, intente denuevo")
            continue

def print_lista(lista):
    if len(lista) > 0:
        print(f"║{lista[0]:^20}", end="")
        print_lista(lista[1:])

def get_destinos():
    print("--- Seleccione un destino ---")
    print(f"{print_lista(referenciaDestinos)}")
    mostrar_informacion("Archivos/Destinos.txt")
    op = int(input("Seleccion: "))
    return op

def get_aerolineas():
    print("--- Seleccione una aerolinea ---")
    print(f"{print_lista(referenciaAerolinea)}")
    mostrar_informacion("Archivos/Aerolinea.txt")
    op = int(input("Seleccion: "))
    return op

def show_results(data):
    if data is None:
        print("\nNo se encontró ningún vuelo con ese dato.")
        return
    aero = obtener_lista_por_dato(data[1], "Archivos/Aerolinea.txt")
    if aero is None:
        aero = ["0", "DESCONOCIDO"]
    dest = obtener_lista_por_dato(data[2], "Archivos/Destinos.txt")
    if dest is None:
        dest = ["0", "DESCONOCIDO"]
    data[1] = aero[1]
    data[2] = dest[1]
    print(f"╔{'═'*20}╦{'═'*20}╦{'═'*20}╦{'═'*20}╦{'═'*20}╗")
    print(f"{print_lista(referenciaVuelos)}")
    print(f"╠{'═'*20}╬{'═'*20}╬{'═'*20}╬{'═'*20}╬{'═'*20}╣")
    print(f"{print_lista(data)}")
    print(f"╚{'═'*20}╩{'═'*20}╩{'═'*20}╩{'═'*20}╩{'═'*20}╝")


# CREATE

def registrar_vuelo():
    print("\n--- Registro de Vuelo ---")
    nuevo = []
    nuevo_id = getNewId()
    nuevo.append(nuevo_id)

    aero = get_aerolineas()
    max_aero = obtener_max_archivo("Archivos/Aerolinea.txt")
    if not existe_referencia_recursiva(max_aero, aero):
        print("ERROR: La aerolínea seleccionada no existe.")
        return
    nuevo.append(aero)

    dest = get_destinos()
    max_dest = obtener_max_archivo("Archivos/Destinos.txt")
    if not existe_referencia_recursiva(max_dest, dest):
        print("ERROR: El destino seleccionado no existe.")
        return
    nuevo.append(dest)

    fecha = get_fecha()
    nuevo.append(fecha)



    guardar_data(archivo_modulo, nuevo)
    print("Vuelo registrado con ID:", nuevo_id)
    return nuevo_id

# READ
def mostrar_vuelos():
    print("\n--- Lista de Vuelos ---")
    print_lista(referenciaVuelos)
    print()
    print("="*80)
    get_vuelos()

def buscar_vuelo():
    found = []
    print("\n--- Buscar Vuelos ---")
    criterio = int(input("Seleccione por que valor quiere buscar: \n1. Aerolineas \n2. Destinos \n"))
    match criterio:
        case 1:
            elec = get_aerolineas()
            found = get_vuelo_by_referencia(criterio,elec)
        case 2: 
            elec = get_destinos()
            found = get_vuelo_by_referencia(criterio,elec)
        case _:
            print("Opcion incorrecta")
    show_results(found)

# UPDATE
def actualizar_vuelo():
    vuelo = []
    mostrar_vuelos()
    try:
        vid = int(input("Ingrese ID del vuelo a actualizar: "))

        op = input(f"Elija una opción: \n1. Cambiar aerolinea \n2. Cambiar destino \n3. Cambiar fecha de llegada\n")
        match op:
            case "1":
                aero = get_aerolineas()
                modificar_lista(archivo_modulo, aero, op, vid)
            case "2":
                dest = get_destinos()
                modificar_lista(archivo_modulo, dest, op, vid)
            case "3":
                fecha = get_fecha()
                modificar_lista(archivo_modulo, fecha, op, vid)
    
    except ValueError:
        print("ID inválido.")

def eliminar_vuelo():
    mostrar_vuelos()
    while True:
        try:
            vid = int(input("Ingrese ID del vuelo a eliminar: "))
            lista = get_vuelo_by_referencia(0, vid)
            print("Este es el vuelo que quiere borrar:")
            print(lista)
            print("¿Esta seguro que quiere borrarlo")
            op = str(input("s/n "))
            if op == "s":
                borrar_data(archivo_modulo,vid,lista)
            elif op == "n":
                print("Volviendo al menu...")
            else:
                print("Opcion invalida")

        except ValueError:
            print("ID inválido.")
        return None

def menu_vuelo():
    while True:
        print("\n--- Menú Vuelos ---")
        print("1. Registrar vuelo")
        print("2. Mostrar vuelos")
        print("3. Buscar vuelo")
        print("4. Actualizar vuelo")
        print("5. Eliminar vuelo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                registrar_vuelo()
            case "2":
                mostrar_vuelos()
            case "3":
                buscar_vuelo()
            case "4":
                actualizar_vuelo()
            case "5":
                eliminar_vuelo()
            case "6":
                print("Saliendo del menú de vuelos...")
                break
            case _:
                print("Opción inválida.")
                continue
