from data import referenciaVuelos, Vuelos, Destinos, Aerolinea, referenciaDestinos,referenciaAerolinea
from CRUDs.Destinos import mostrar_destinos 
from Helpers.Validaciones import validar_fecha

def get_fecha():
    while True:
        try:
            fecha = input("Ingrese fecha de llegada (AAAA-MM-DD): ")
            return fecha
        except ValueError:
            print("Fecha invalida, intente denuevo")
            continue
def get_new_id_vuelo():
    return len(Vuelos) + 1
def get_destinos():
    print("--- Seleccione un destino ---")
    print(f"{referenciaDestinos[0]:<5} {referenciaDestinos[1]:<20}")
    for i in Destinos:
        print(f"{i[0]:<5} {i[1]:<20}")
    op = int(input("Seleccion: "))
    return Destinos[op-1][0]
def get_aerolineas():
    print("--- Seleccione una aerolinea ---")
    print(f"{referenciaAerolinea[0]:<5} {referenciaAerolinea[1]:<20}")
    for i in Aerolinea:
        print(f"{i[0]:<5} {i[1]:<20}")
    op = int(input("Seleccion: "))
    return Aerolinea[op-1][0]
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
    nuevo_id = get_new_id_vuelo()
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

    Vuelos.append(nuevo)
    print("Vuelo registrado con ID:", nuevo_id)
    return nuevo_id

# READ
def mostrar_vuelos():
    print("\n--- Lista de Vuelos ---")
    print("ID | Empresa | Destino | Fecha | Escala")
    for v in Vuelos:
        destino = "N/A"
        for d in Destinos:
            if d[0] == v[2]:
                destino = d[1]
        print(v[0], "-", v[1], "-", destino, "-", v[3], "-", v[4])


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
    mostrar_vuelos()
    try:
        vid = int(input("Ingrese ID del vuelo a actualizar: "))
        for v in Vuelos:
            if v[0] == vid:
                print("Vuelo actual:", v[1], "-", v[2], "-", v[3], "-", v[4])
                nueva_emp = input("Nueva empresa (Enter para mantener): ")
                if nueva_emp != "":
                    v[1] = nueva_emp
                mostrar_destinos()
                nuevo_dest = input("Nuevo ID destino (Enter para mantener): ")
                if nuevo_dest != "":
                    try:
                        nuevo_dest = int(nuevo_dest)
                        existe = False
                        for d in Destinos:
                            if d[0] == nuevo_dest:
                                existe = True
                        if existe:
                            v[2] = nuevo_dest
                    except ValueError:
                        print("Destino inválido, se mantiene el anterior.")
                nueva_fecha = get_fecha()
                v[3] = nueva_fecha
                nueva_escala = input("Nueva escala (Enter para mantener): ")
                if nueva_escala != "":
                    v[4] = nueva_escala
                print("Vuelo actualizado.")
                return vid
        print("No se encontró vuelo con ese ID.")
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