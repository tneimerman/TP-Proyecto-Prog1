from data import referenciaVuelos, Vuelos, Destinos, Aerolinea, referenciaDestinos,referenciaAerolinea
from CRUDs.Destinos import mostrar_destinos 
from Helpers import validar_fecha
from CRUDs.Archivos import *
archivo_modulo = "Archivos/Vuelos.txt"
#
def get_vuelos(dest,aero):
    try:
        arch = open(archivo_modulo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            for d in dest:
                if lista[1] == d[0]:
                    lista[1] == d[1]
            for a in aero:
                if lista[2] == a[0]:
                    lista[2] == a[1]
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
    print_info("Archivos/Destinos.txt")
    op = int(input("Seleccion: "))
    return op
def get_aerolineas():
    print("--- Seleccione una aerolinea ---")
    print(f"{print_lista(referenciaAerolinea)}")
    print_info("Archivos/Aerolinea.txt")
    op = int(input("Seleccion: "))
    return op
    
def show_results(data):
    
    aero = get_lista_by_dato(data[1], "Archivos/Aerolinea.txt")
    dest = get_lista_by_dato(data[2], "Archivos/Destinos.txt")
    data[1] = aero[1]
    data[2] = dest[1]
    print(f"╔{"═"*20}╦{"═"*20}╦{"═"*20}╦{"═"*20}╦{"═"*20}╗")
    print(f"{print_lista(referenciaVuelos)}")
    print(f"╠{"═"*20}╬{"═"*20}╬{"═"*20}╬{"═"*20}╬{"═"*20}╣")
    print(f"{print_lista(data)}")
    print(f"╚{"═"*20}╩{"═"*20}╩{"═"*20}╩{"═"*20}╩{"═"*20}╝")

    
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

    fecha = get_fecha()
    nuevo.append(fecha)

    escala = input("Ingrese escala (Directo o con escala): ")
    nuevo.append(escala)

    save_data(archivo_modulo, nuevo)
    print("Vuelo registrado con ID:", nuevo_id)
    return nuevo_id

# READ

def mostrar_vuelos():
    aero = get_matriz("Archivos/Aerolinea.txt")
    dest = get_matriz("Archivos/Destinos.txt")
    print("\n--- Lista de Vuelos ---")
    print(f"║{print_lista(referenciaVuelos)}║")
    print("="*110)
    print(f"{get_vuelos(dest,aero)}")



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
    while True:
        try:
            vid = int(input("Ingrese ID del vuelo a eliminar: "))
            lista = get_vuelo_by_referencia(0, vid)
            print("Este es el vuelo que quiere borrar:")
            print(lista)
            print("¿Esta seguro que quiere borrarlo")
            op = str(input("s/n "))
            if op == "s":
                delete_data(archivo_modulo,vid,lista)
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
                print("Opción inválida.")
                continue