from data import referenciaVuelos, Vuelos, Destinos, Aerolinea, referenciaDestinos,referenciaAerolinea
from CRUDs.Destinos import mostrar_destinos 

def get_new_id_vuelo():
    if len(Vuelos) == 0:
        return 1
    ids = []
    for v in Vuelos:
        ids.append(v[0])
    return max(ids) + 1
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
    for x in Vuelos:
        if x[pos] == ref:
            return x
def show_results(data):
    for aero in Aerolinea:
        if aero[0] == data[1]:
            data[1] = aero[1]
            break
    for dest in Destinos:
        if dest[0] == data[2]:
            data[2] = dest[1]
            break
    print(f"╔{"="*58}╗")
    print(f"║{"Aerolinea":<10}║{"Destino":<10}║{referenciaVuelos[3]:<15}║{referenciaVuelos[4]:<20}║")
    print(f"╠{"="*58}╣")
    print(f"║{data[1]:<10}║{data[2]:<10}║{data[3]:<15}║{data[4]:<20}║")
    print(f"╚{"="*58}╝")

    
# CREATE
def registrar_vuelo():
    print("\n--- Registro de Vuelo ---")
    nuevo = []
    nuevo_id = get_new_id_vuelo()
    nuevo.append(nuevo_id)

    empresa = input("Ingrese nombre de la empresa: ")
    nuevo.append(empresa)

    # IDDestino (validar que exista)
    mostrar_destinos()
    try:
        iddest = int(input("Ingrese ID del destino: "))
        existe = False
        for d in Destinos:
            if d[0] == iddest:
                existe = True
        if not existe:
            print("Ese destino no existe.")
            return None
        nuevo.append(iddest)
    except ValueError:
        print("ID destino inválido.")
        return None

    fecha = input("Ingrese fecha de llegada (AAAA-MM-DD): ")
    nuevo.append(fecha)

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
    found = 0
    print("\n--- Buscar Vuelos ---")
    criterio = int(input("Seleccione por que valor quiere buscar: \n1. Destinos \n2. Aerolineas \n"))
    match criterio:
        case 1:
            elec = get_destinos()
            found = get_ref_vuelo(1,elec)
        case 2: 
            elec = get_aerolineas()
            found = get_ref_vuelo(2,elec)
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
                nueva_fecha = input("Nueva fecha (AAAA-MM-DD, Enter para mantener): ")
                if nueva_fecha != "":
                    v[3] = nueva_fecha
                nueva_escala = input("Nueva escala (Enter para mantener): ")
                if nueva_escala != "":
                    v[4] = nueva_escala
                print("Vuelo actualizado.")
                return vid
        print("No se encontró vuelo con ese ID.")
    except ValueError:
        print("ID inválido.")
    return None


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

        if opcion == "1":
            registrar_vuelo()
        elif opcion == "2":
            mostrar_vuelos()
        elif opcion == "3":
            buscar_vuelo()
        elif opcion == "4":
            actualizar_vuelo()
        elif opcion == "5":
            eliminar_vuelo()
        elif opcion == "6":
            print("Saliendo del menú de vuelos...")
            break
        else:
            print("Opción inválida.")