from data import referenciaVuelos, Vuelos, Destinos
from CRUDs.Destinos import mostrar_destinos 

def getNewIdVuelo():
    if len(Vuelos) == 0:
        return 1
    ids = []
    for v in Vuelos:
        ids.append(v[0])
    return max(ids) + 1

# CREATE
def registrar_vuelo():
    print("\n--- Registro de Vuelo ---")
    nuevo = []
    nuevo_id = getNewIdVuelo()
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
    criterio = input("Ingrese empresa o destino a buscar: ")
    encontrados = []
    for v in Vuelos:
        destino = ""
        for d in Destinos:
            if d[0] == v[2]:
                destino = d[1]
        if criterio in v[1] or criterio in destino:
            encontrados.append(v)
    if len(encontrados) > 0:
        print("\nResultados:")
        for v in encontrados:
            destino = "N/A"
            for d in Destinos:
                if d[0] == v[2]:
                    destino = d[1]
            print("ID:", v[0], "-", v[1], "→", destino, v[3], "(", v[4], ")")
    else:
        print("No se encontraron coincidencias.")

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


def menuVuelos():
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
            print("Opción inválida.")
