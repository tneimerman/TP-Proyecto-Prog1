from data import referenciaVueloPasajero, VueloPasajero, vuelo_pasajero
from data import referenciaPasajeros, Pasajeros
from data import referenciaVuelos, Vuelos
from data import referenciaDestinos, Destinos
from data import referenciaAerolinea, Aerolinea
import re
from functools import reduce

def obtener_nuevo_id():
    """Obtiene el siguiente ID disponible para VueloPasajero"""
    if not VueloPasajero:
        return 1
    ids_existentes = list(map(lambda x: x[0], VueloPasajero))
    return max(ids_existentes) + 1

# Validaciones de IDs en las matrices
def validar_id_pasajero(id_pasajero):
    ids_pasajeros = list(map(lambda x: x[0], Pasajeros))
    return id_pasajero in ids_pasajeros

def validar_id_vuelo(id_vuelo):
    ids_vuelos = list(map(lambda x: x[0], Vuelos))
    return id_vuelo in ids_vuelos

def obtener_nombre_pasajero(id_pasajero):
    pasajero = list(filter(lambda x: x[0] == id_pasajero, Pasajeros))
    if pasajero:
        return f"{pasajero[0][4]} {pasajero[0][5]}"  # Nombre + Apellido
    return "Desconocido"

def obtener_info_vuelo(id_vuelo):
    """Obtiene información del vuelo por ID"""
    vuelo = list(filter(lambda x: x[0] == id_vuelo, Vuelos))
    if vuelo:
        empresa = vuelo[0][1]
        id_destino = vuelo[0][2]
        fecha = vuelo[0][3]
        
        # Obtener destino
        destino = list(filter(lambda x: x[0] == id_destino, Destinos))
        nombre_destino = destino[0][1] if destino else "Desconocido"
        
        return f"{empresa} - {nombre_destino} ({fecha})"
    return "Vuelo desconocido"

# CRUD - INSERTAR NUEVA RELACION VUELO-PASAJERO

def crear_relacion_vuelo_pasajero():
    """Crea una nueva relación vuelo-pasajero"""
    print("\n=== CREAR NUEVA RELACIÓN VUELO-PASAJERO ===")
    
    # Mostrar pasajeros disponibles
    print("\nPasajeros disponibles:")
    for pasajero in Pasajeros:
        print(f"ID: {pasajero[0]} - {pasajero[4]} {pasajero[5]} ({pasajero[2]})")
    
    try:
        id_pasajero = int(input("\nIngrese ID del pasajero: "))
        if not validar_id_pasajero(id_pasajero):
            print("Error: ID de pasajero no válido")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    # Mostrar vuelos disponibles
    print("\nVuelos disponibles:")
    for vuelo in Vuelos:
        destino = list(filter(lambda x: x[0] == vuelo[2], Destinos))
        nombre_destino = destino[0][1] if destino else "Desconocido"
        print(f"ID: {vuelo[0]} - {vuelo[1]} a {nombre_destino} ({vuelo[3]})")
    
    try:
        id_vuelo = int(input("\nIngrese ID del vuelo: "))
        if not validar_id_vuelo(id_vuelo):
            print("Error: ID de vuelo no válido")
            return
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    # Verificar si la relación ya existe
    relacion_existente = list(filter(lambda x: x[1] == id_pasajero and x[2] == id_vuelo, VueloPasajero))
    if relacion_existente:
        print("Error: Esta relación ya existe")
        return
    
    # Crear nueva relación
    nuevo_id = obtener_nuevo_id()
    nueva_relacion = [nuevo_id, id_pasajero, id_vuelo]
    VueloPasajero.append(nueva_relacion)
    
    # Actualizar diccionario
    vuelo_pasajero.append(dict(zip(referenciaVueloPasajero, nueva_relacion)))
    
    print(f"Relación creada exitosamente:")
    print(f"Pasajero: {obtener_nombre_pasajero(id_pasajero)}")
    print(f"Vuelo: {obtener_info_vuelo(id_vuelo)}")

# CRUD - BUSCAR NUEVA RELACION VUELO-PASAJERO

def buscar_relaciones():
    print("\n=== BUSCAR RELACIONES VUELO-PASAJERO ===")
    print("1. Buscar por ID de relación")
    print("2. Buscar por ID de pasajero")
    print("3. Buscar por ID de vuelo")
    print("4. Mostrar todas las relaciones")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    if opcion == 1:
        try:
            id_relacion = int(input("Ingrese ID de la relación: "))
            relaciones = list(filter(lambda x: x[0] == id_relacion, VueloPasajero))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            return
    elif opcion == 2:
        try:
            id_pasajero = int(input("Ingrese ID del pasajero: "))
            relaciones = list(filter(lambda x: x[1] == id_pasajero, VueloPasajero))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            return
    elif opcion == 3:
        try:
            id_vuelo = int(input("Ingrese ID del vuelo: "))
            relaciones = list(filter(lambda x: x[2] == id_vuelo, VueloPasajero))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            return
    elif opcion == 4:
        relaciones = VueloPasajero
    else:
        print("Opción no válida")
        return
    
    if not relaciones:
        print("No se encontraron relaciones")
        return
    
    print(f"\nSe encontraron {len(relaciones)} relación(es):")
    print("-" * 80)
    for relacion in relaciones:
        nombre_pasajero = obtener_nombre_pasajero(relacion[1])
        info_vuelo = obtener_info_vuelo(relacion[2])
        print(f"ID: {relacion[0]} | Pasajero: {nombre_pasajero} | Vuelo: {info_vuelo}")


# CRUD - ACTUALIZAR RELACION VUELO-PASAJERO

def actualizar_relacion():
    """Actualiza una relación vuelo-pasajero existente"""
    print("\n=== ACTUALIZAR RELACIÓN VUELO-PASAJERO ===")
    
    if not VueloPasajero:
        print("No hay relaciones para actualizar")
        return
    
    # Mostrar relaciones existentes
    print("\nRelaciones existentes:")
    for relacion in VueloPasajero:
        nombre_pasajero = obtener_nombre_pasajero(relacion[1])
        info_vuelo = obtener_info_vuelo(relacion[2])
        print(f"ID: {relacion[0]} | Pasajero: {nombre_pasajero} | Vuelo: {info_vuelo}")
    
    try:
        id_relacion = int(input("\nIngrese ID de la relación a actualizar: "))
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    # Buscar la relación
    indice = -1
    for i, relacion in enumerate(VueloPasajero):
        if relacion[0] == id_relacion:
            indice = i
            break
    
    if indice == -1:
        print("Error: Relación no encontrada")
        return
    
    relacion_actual = VueloPasajero[indice]
    print(f"\nRelación actual:")
    print(f"Pasajero: {obtener_nombre_pasajero(relacion_actual[1])}")
    print(f"Vuelo: {obtener_info_vuelo(relacion_actual[2])}")
    
    print("\n¿Qué desea actualizar?")
    print("1. ID del pasajero")
    print("2. ID del vuelo")
    print("3. Ambos")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    nuevo_id_pasajero = relacion_actual[1]
    nuevo_id_vuelo = relacion_actual[2]
    
    if opcion in [1, 3]:
        print("\nPasajeros disponibles:")
        for pasajero in Pasajeros:
            print(f"ID: {pasajero[0]} - {pasajero[4]} {pasajero[5]}")
        
        try:
            nuevo_id_pasajero = int(input("Nuevo ID del pasajero: "))
            if not validar_id_pasajero(nuevo_id_pasajero):
                print("Error: ID de pasajero no válido")
                return
        except ValueError:
            print("Error: Debe ingresar un número válido")
            return
    
    if opcion in [2, 3]:
        print("\nVuelos disponibles:")
        for vuelo in Vuelos:
            destino = list(filter(lambda x: x[0] == vuelo[2], Destinos))
            nombre_destino = destino[0][1] if destino else "Desconocido"
            print(f"ID: {vuelo[0]} - {vuelo[1]} a {nombre_destino}")
        
        try:
            nuevo_id_vuelo = int(input("Nuevo ID del vuelo: "))
            if not validar_id_vuelo(nuevo_id_vuelo):
                print("Error: ID de vuelo no válido")
                return
        except ValueError:
            print("Error: Debe ingresar un número válido")
            return
    
    # Verificar si la nueva relación ya existe (excluyendo la actual)
    relacion_existente = list(filter(lambda x: x[1] == nuevo_id_pasajero and x[2] == nuevo_id_vuelo and x[0] != id_relacion, VueloPasajero))
    if relacion_existente:
        print("Error: Ya existe una relación con estos datos")
        return
    
    # Actualizar la relación
    VueloPasajero[indice] = [id_relacion, nuevo_id_pasajero, nuevo_id_vuelo]
    
    # Actualizar diccionario
    for i, item in enumerate(vuelo_pasajero):
        if item['ID'] == id_relacion:
            vuelo_pasajero[i] = dict(zip(referenciaVueloPasajero, VueloPasajero[indice]))
            break
    
    print("✅ Relación actualizada exitosamente:")
    print(f"   Pasajero: {obtener_nombre_pasajero(nuevo_id_pasajero)}")
    print(f"   Vuelo: {obtener_info_vuelo(nuevo_id_vuelo)}")

# CRUD - ELIMINAR RELACION VUELO-PASAJERO

def eliminar_relacion():
    """Elimina una relación vuelo-pasajero"""
    print("\n=== ELIMINAR RELACIÓN VUELO-PASAJERO ===")
    
    if not VueloPasajero:
        print("No hay relaciones para eliminar")
        return
    
    # Mostrar relaciones existentes
    print("\nRelaciones existentes:")
    for relacion in VueloPasajero:
        nombre_pasajero = obtener_nombre_pasajero(relacion[1])
        info_vuelo = obtener_info_vuelo(relacion[2])
        print(f"ID: {relacion[0]} | Pasajero: {nombre_pasajero} | Vuelo: {info_vuelo}")
    
    try:
        id_relacion = int(input("\nIngrese ID de la relación a eliminar: "))
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    # Buscar y eliminar la relación
    relacion_encontrada = None
    for i, relacion in enumerate(VueloPasajero):
        if relacion[0] == id_relacion:
            relacion_encontrada = VueloPasajero.pop(i)
            break
    
    if relacion_encontrada is None:
        print("Error: Relación no encontrada")
        return
    
    # Eliminar del diccionario
    vuelo_pasajero[:] = [item for item in vuelo_pasajero if item['ID'] != id_relacion]
    
    print("Relación eliminada exitosamente:")
    print(f"Pasajero: {obtener_nombre_pasajero(relacion_encontrada[1])}")
    print(f"Vuelo: {obtener_info_vuelo(relacion_encontrada[2])}")

# FUNCIONES DE ESTADÍSTICAS Y REPORTES

def generar_estadisticas():
    print("\n=== ESTADÍSTICAS DEL SISTEMA ===")
    
    if not VueloPasajero:
        print("No hay datos para generar estadísticas")
        return
    
    print("1. Pasajero con más vuelos")
    print("2. Vuelo con más pasajeros")
    print("3. Destinos más populares")
    print("4. Estadísticas por empresa")
    print("5. Todas las estadísticas")
    
    try:
        opcion = int(input("\nSeleccione una opción: "))
    except ValueError:
        print("Error: Debe ingresar un número válido")
        return
    
    if opcion in [1, 5]:
        # Pasajero con más vuelos
        ids_pasajeros = list(map(lambda x: x[1], VueloPasajero))
        pasajeros_unicos = list(set(ids_pasajeros))
        
        conteos_pasajeros = list(map(lambda pid: (pid, len(list(filter(lambda x: x[1] == pid, VueloPasajero)))), pasajeros_unicos))
        
        if conteos_pasajeros:
            pasajero_top = reduce(lambda a, b: a if a[1] > b[1] else b, conteos_pasajeros)
            nombre_pasajero = obtener_nombre_pasajero(pasajero_top[0])
            print(f"\nPasajero con más vuelos: {nombre_pasajero} ({pasajero_top[1]} vuelos)")
    
    if opcion in [2, 5]:
        # Vuelo con más pasajeros
        ids_vuelos = list(map(lambda x: x[2], VueloPasajero))
        vuelos_unicos = list(set(ids_vuelos))
        
        conteos_vuelos = list(map(lambda vid: (vid, len(list(filter(lambda x: x[2] == vid, VueloPasajero)))), vuelos_unicos))
        
        if conteos_vuelos:
            vuelo_top = reduce(lambda a, b: a if a[1] > b[1] else b, conteos_vuelos)
            info_vuelo = obtener_info_vuelo(vuelo_top[0])
            print(f"\nVuelo con más pasajeros: {info_vuelo} ({vuelo_top[1]} pasajeros)")
    
    if opcion in [3, 5]:
        # Destinos más populares
        vuelos_con_destino = list(map(lambda vp: next(filter(lambda v: v[0] == vp[2], Vuelos), None), VueloPasajero))
        vuelos_validos = list(filter(lambda x: x is not None, vuelos_con_destino))
        
        if vuelos_validos:
            ids_destinos = list(map(lambda v: v[2], vuelos_validos))
            destinos_unicos = list(set(ids_destinos))
            
            conteos_destinos = list(map(lambda did: (did, len(list(filter(lambda x: x == did, ids_destinos)))), destinos_unicos))
            conteos_destinos.sort(key=lambda x: x[1], reverse=True)
            
            print(f"\nDestinos más populares:")
            for destino_id, cantidad in conteos_destinos:
                destino = list(filter(lambda x: x[0] == destino_id, Destinos))
                nombre_destino = destino[0][1] if destino else "Desconocido"
                print(f"   {nombre_destino}: {cantidad} reservas")
    
    if opcion in [4, 5]:
        # Estadísticas por empresa
        vuelos_con_empresa = list(map(lambda vp: next(filter(lambda v: v[0] == vp[2], Vuelos), None), VueloPasajero))
        vuelos_validos = list(filter(lambda x: x is not None, vuelos_con_empresa))
        
        if vuelos_validos:
            empresas = list(map(lambda v: v[1], vuelos_validos))
            empresas_unicas = list(set(empresas))
            
            conteos_empresas = list(map(lambda emp: (emp, len(list(filter(lambda x: x == emp, empresas)))), empresas_unicas))
            conteos_empresas.sort(key=lambda x: x[1], reverse=True)
            
            print(f"\n📊 Estadísticas por empresa:")
            for empresa, cantidad in conteos_empresas:
                print(f"   {empresa}: {cantidad} reservas")

def mostrar_menu():
    print("\n" + "="*50)
    print("--- Menú Gestión de Relaciones Vuelo-Pasajero ---")
    print("="*50)
    print("1. Crear nueva relación")
    print("2. Buscar relaciones")
    print("3. Actualizar relación")
    print("4. Eliminar relación")
    print("5. Ver estadísticas")
    print("0. Salir")
    print("="*50)

def menu_vuelo_pasajero():
    print("¡Bienvenido al Sistema de Gestión de Relaciones Vuelo-Pasajero!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Debe ingresar un número válido")
            continue
        
        if opcion == 1:
            crear_relacion_vuelo_pasajero()
        elif opcion == 2:
            buscar_relaciones()
        elif opcion == 3:
            actualizar_relacion()
        elif opcion == 4:
            eliminar_relacion()
        elif opcion == 5:
            generar_estadisticas()
        elif opcion == 0:
            print("Volviendo al menú...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
        
        input("\nPresione Enter para continuar...")
