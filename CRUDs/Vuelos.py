from data import referenciaVuelos, Vuelos, Destinos, Aerolinea, referenciaDestinos,referenciaAerolinea
from CRUDs.Destinos import mostrar_destinos 
from Helpers import validar_fecha
from CRUDs.Archivos import *
archivo_modulo = "Archivos/Vuelos.txt"
def get_vuelos(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            aero = get_lista_by_dato(lista[1], "Archivos/Aerolinea.txt")
            dest = get_lista_by_dato(lista[2], "Archivos/Destinos.txt")
            lista[1] = aero[1]
            lista[2] = dest[1]
            for x in lista:
                print(f"||{x:<20}||", end = " ")
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
    print_info("Archivos/Destinos.txt")
    op = int(input("Seleccion: "))
    return op
def get_aerolineas():
    print("--- Seleccione una aerolinea ---")
    print(f"{print_lista(referenciaAerolinea)}")
    print_info("Archivos/Aerolinea.txt")
    op = int(input("Seleccion: "))
    return op
def get_ref_vuelo(pos, ref):
    vuelo = []
    for x in Vuelos:
        if x[pos] == ref:
            vuelo.append(x)
    return vuelo
    
def show_results(data):

    print(f"╔{"═"*10}╦{"═"*10}╦{"═"*15}╦{"═"*20}╗")
    print(f"║{"Aerolinea":<10}║{"Destino":<10}║{referenciaVuelos[3]:<15}║{referenciaVuelos[4]:<20}║")
    for x in data:
        for aero in Aerolinea:
            if aero[0] == x[1]:
                x[1] = aero[1]
            break
        for dest in Destinos:
            if dest[0] == x[2]:
                x[2] = dest[1]
                break
   
        print(f"╠{"═"*10}╬{"═"*10}╬{"═"*15}╬{"═"*20}╣")
        print(f"║{x[1]:<10}║{x[2]:<10}║{x[3]:<15}║{x[4]:<20}║")
    print(f"╚{"═"*10}╩{"═"*10}╩{"═"*15}╩{"═"*20}╝")

    
# CREATE
def registrar_vuelo():
    print("\n--- Registro de Vuelo ---")
    nuevo = []
    nuevo_id = get_max_id(archivo_modulo)
    nuevo.append(nuevo_id)

    aero = get_aerolineas()
    nuevo.append(aero)
    dest = get_destinos()
    nuevo.append(dest)
    while True:
        try:
            fecha = input("Ingrese fecha de llegada (AAAA-MM-DD): ")
            nuevo.append(fecha)
            break
        except ValueError:
            print("Fecha invalida, intente denuevo")
            continue

    escala = input("Ingrese escala (Directo o con escala): ")
    nuevo.append(escala)

    save_data(archivo_modulo, nuevo)
    print("Vuelo registrado con ID:", nuevo_id)
    return nuevo_id

# READ

def mostrar_vuelos():
    print("\n--- Lista de Vuelos ---")
    print(f"||{print_lista(referenciaVuelos)}||")
    print("="*124)
    get_vuelos(archivo_modulo)



def buscar_vuelo():
    found = []
    print("\n--- Buscar Vuelos ---")
    criterio = int(input("Seleccione por que valor quiere buscar: \n1. Aerolineas \n2. Destinos \n"))
    match criterio:
        case 1:
            elec = get_aerolineas()
            found = get_ref_vuelo(criterio,elec)
        case 2: 
            elec = get_destinos()
            found = get_ref_vuelo(criterio,elec)
        case _:
            print("Opcion incorrecta")
    show_results(found)
    
        
            
   

# UPDATE
def actualizar_vuelo():
    vuelo = []
    mostrar_vuelos()
    try:
        vid = int(input("Ingrese ID del vuelo a actualizar: "))
        for v in Vuelos:
            if vid == v[0]:
                vuelo = v
                break
        op = input(f"Elija una opción: \n1. Cambiar aerolinea \n2. Cambiar destino \n3. Cambiar fecha de llegada \n4. Cambiar escala \n")
        match op:
            case "1":
                aero = get_aerolineas()
                Vuelos[vuelo[0]][1] = aero
            case "2":
                dest = get_destinos()
                Vuelos[vuelo[0]][2] = dest
            case "3":
                fecha = get_fecha()
                Vuelos[vuelo[0]][3] = fecha
            case "4":
                escala = input("Ingrese escala (Directo o con escala): ")
                Vuelos[vuelo[0]][4] = escala
    
    except ValueError:
        print("ID inválido.")


def eliminar_vuelo():
    mostrar_vuelos()
    try:
        vid = int(input("Ingrese ID del vuelo a eliminar: "))
        for v in Vuelos:
            if v[0] == vid:
                Vuelos.remove(v)
                print("Vuelo eliminado.")
                return vid
        print("No se encontró vuelo con ese ID.")
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
                print("Opción inválida.")
                continue