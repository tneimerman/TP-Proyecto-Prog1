from data import referenciaAerolinea
import re
from functools import reduce
from CRUDs.Archivos import * 
archivo_modulo = "Archivos/Aerolinea.txt"
def registrar_aerolinea():
    """Registra una nueva aerolinea en el sistema"""
    print("\n--- Registro de Aerolinea ---")
    nueva_aerolinea = []
    nuevo_id = get_max_id()
    nueva_aerolinea.append(nuevo_id)
    
    # Validar nombre de la Aerolinea
    while True:
        nombre = input("Ingrese el nombre de la aerolinea: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
            continue
            
        # Usamos un filtro para verificar si ya existe
        nombres_existentes = list(filter(lambda x: x[1].lower() == nombre.lower(), Aerolinea))
        if nombres_existentes:
            print("Ya existe una aerolinea con ese nombre.")
        else:
            nueva_aerolinea.append(nombre)
            break
    
    # Validar modelo con expresiones regulares
    while True:
        modelo = input("Ingrese el modelo de la aeronave: ").strip()
        # Validar que contenga letras y numeros (formato del modelo de avion)
        if re.match(r'^[A-Za-z0-9\s\-]+$', modelo) and len(modelo) >= 3:
            nueva_aerolinea.append(modelo)
            break
        else:
            print("Modelo invalido. Debe contener al menos 3 caracteres ya sea letras, numeros, espacios y guiones.")
    
    Aerolinea.append(nueva_aerolinea)
    print(f"Aerolinea registrada correctamente con el ID: {nuevo_id}")
    return nuevo_id

# -------- Metodo de busqueda --------
def buscar_aerolineas():
    if not Aerolinea:
        print("No hay aerolineas registradas.")
        return
    
    print("\n--- Buscar Aerolineas ---")
    print("1. Mostrar todas")
    print("2. Buscar por ID")
    print("3. Buscar por nombre")
    print("4. Buscar por modelo")
    
    opcion = input("Seleccione opcion de busqueda: ")
    
    if opcion == "1":
        mostrar_todas_aerolineas()
    elif opcion == "2":
        buscar_por_id()
    elif opcion == "3":
        buscar_por_nombre()
    elif opcion == "4":
        print("deshabilitado por el momento")
        # buscar_por_modelo()
    else:
        print("Opcion invalida.")

def mostrar_todas_aerolineas():
    print(f"\n{'='*60}")
    print(f"{'ID':<5} {'NOMBRE':<25} {'MODELO':<25}")
    print(f"{'='*60}")
    
    # Usamos el metodo map para formatear la salida
    aerolineas_formateadas = list(map(
        lambda x: f"{x[0]:<5} {x[1]:<25} {x[2]:<25}", 
        Aerolinea
    ))
    
    for linea in aerolineas_formateadas:
        print(linea)
    
    # Usar reduce para contar total
    total = reduce(lambda acc, x: acc + 1, Aerolinea, 0)
    print(f"{'='*60}")
    print(f"Total de aerolineas: {total}")

def buscar_por_id():
    """Busca una aerolinea por su ID"""
    try:
        id_buscar = int(input("Ingrese el ID a buscar: "))
        resultado = list(filter(lambda x: x[0] == id_buscar, Aerolinea))
        
        if resultado:
            aerolinea = resultado[0]
            print(f"\n Aerolinea encontrada:")
            print(f"ID: {aerolinea[0]}")
            print(f"Nombre: {aerolinea[1]}")
            print(f"Modelo: {aerolinea[2]}")
        else:
            print("No se encontro aerolinea con ese ID.")
    except ValueError:
        print("ID invalido. Debe ser un numero.")

def buscar_por_nombre():
    nombre_buscar = input("Ingrese el nombre a buscar: ").strip().lower()
    
    resultados = list(filter(
        lambda x: re.search(nombre_buscar, x[1].lower()), 
        Aerolinea
    ))
    
    if resultados:
        print(f"\n Se encontraron {len(resultados)} aerolinea(s):")
        for aerolinea in resultados:
            print(f"ID: {aerolinea[0]} - {aerolinea[1]} - {aerolinea[2]}")
    else:
        print("No se encontraron aerolineas con ese nombre.")

# -------- MODIFICAR --------
def actualizar_aerolinea():
    """Actualizar los datos de una aerolinea existente"""
    if not Aerolinea:
        print("No hay aerolineas registradas.")
        return
    
    print("\n--- Actualizar Aerolinea ---")
    try:
        id_actualizar = int(input("Ingrese el ID de la aerolinea a actualizar: "))
        
        # Buscar la aerolinea
        indice = -1
        for i, aerolinea in enumerate(Aerolinea):
            if aerolinea[0] == id_actualizar:
                indice = i
                break
        
        if indice == -1:
            print("No se encontro aerolinea con ese ID.")
            return
        
        aerolinea_actual = Aerolinea[indice]
        print(f"\n Datos actuales:")
        print(f"ID: {aerolinea_actual[0]}")
        print(f"Nombre: {aerolinea_actual[1]}")
        print(f"Modelo: {aerolinea_actual[2]}")
        
        print("\n ¿Que desea actualizar?")
        print("1. Nombre")
        print("2. Modelo")
        print("3. Ambos")
        
        opcion = input("Seleccione opcion: ")
        
        if opcion in ["1", "3"]:
            while True:
                nuevo_nombre = input(f"Nuevo nombre (actual: {aerolinea_actual[1]}): ").strip()
                if not nuevo_nombre:
                    print("El nombre no puede estar vacio.")
                    continue
                
                # Verificar que no exista otro con el mismo nombre
                otros_con_nombre = list(filter(
                    lambda x: x[1].lower() == nuevo_nombre.lower() and x[0] != id_actualizar, 
                    Aerolinea
                ))
                
                if otros_con_nombre:
                    print("Ya existe otra aerolinea con ese nombre.")
                else:
                    Aerolinea[indice][1] = nuevo_nombre
                    break
        
        if opcion in ["2", "3"]:
            while True:
                nuevo_modelo = input(f"Nuevo modelo (actual: {aerolinea_actual[2]}): ").strip()
                if re.match(r'^[A-Za-z0-9\s\-]+$', nuevo_modelo) and len(nuevo_modelo) >= 3:
                    Aerolinea[indice][2] = nuevo_modelo
                    break
                else:
                    print("Modelo invalido. Debe contener al menos 3 caracteres.")
        
        if opcion in ["1", "2", "3"]:
            print("Aerolinea actualizada exitosamente.")
        else:
            print("Opcion invalida.")
            
    except ValueError:
        print("ID invalido. Debe ser un numero.")

# -------- BORRADO --------
def eliminar_aerolinea():
    """Elimina una aerolinea del sistema"""
    if not Aerolinea:
        print("No hay aerolneas registradas.")
        return
    
    print("\n--- Eliminar Aerolinea ---")
    try:
        id_eliminar = int(input("Ingrese el ID de la aerolinea a eliminar: "))
        
        # Buscar la aerolinea
        aerolinea_encontrada = None
        for aerolinea in Aerolinea:
            if aerolinea[0] == id_eliminar:
                aerolinea_encontrada = aerolinea
                break
        
        if aerolinea_encontrada:
            print(f"\nAerolínea a eliminar:")
            print(f"ID: {aerolinea_encontrada[0]}")
            print(f"Nombre: {aerolinea_encontrada[1]}")
            print(f"Modelo: {aerolinea_encontrada[2]}")
            
            confirmacion = input("\n¿Esta seguro de eliminar esta aerolinea? (s/n): ").lower()
            
            if confirmacion == 's':
                Aerolinea.remove(aerolinea_encontrada)
                print("Aerolinea eliminada exitosamente.")
                return id_eliminar
            else:
                print("Eliminacion cancelada.")
        else:
            print("No se encontro aerolinea con ese ID.")
            
    except ValueError:
        print("ID invalido. Debe ser un numero.")
    
    return None

# -------- ESTADISTICAS --------
def mostrar_estadisticas():
    """Muestra estadisticas del sistema"""
    if not Aerolinea:
        print("No hay aerolineas registradas.")
        return
    
    print("\n--- Estadisticas del Sistema ---")
    
    # Total de aerolineas
    total = len(Aerolinea)
    print(f"Total de aerolineas: {total}")
    
    # Aerolinea con nombre mas largo usando max
    nombre_mas_largo = max(Aerolinea, key=lambda x: len(x[1]))
    print(f"\nAerolinea con nombre mas largo: {nombre_mas_largo[1]} ({len(nombre_mas_largo[1])} caracteres)")

# -------- MENU--------
def menu_aerolineas():
    """Menu principal del sistema CRUD de aerolineas"""
    salir = False
    
    while not salir:
        print()
        print("\n" + "="*50)
        print("--- Menú Gestión de Aerolineas ---")
        print("="*50)
        print("1. Registrar nueva aerolinea")
        print("2. Buscar aerolineas")
        print("3. Actualizar aerolinea")
        print("4. Eliminar aerolinea")
        print("5. Mostrar estadisticas")
        print("0. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opcion: ").strip()
        
        if opcion == "1":
            registrar_aerolinea()
        elif opcion == "2":
            buscar_aerolineas()
        elif opcion == "3":
            actualizar_aerolinea()
        elif opcion == "4":
            eliminar_aerolinea()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "0":
            print("Volviendo al menú...")
            print()
            salir = True
        else:
            print("Opcion invalida. Por favor seleccione una opcion del 1 al 6.")

# Ejecutar