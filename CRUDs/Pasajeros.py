from data import referenciaPasajeros, Pasajeros
import re

def getNewId():
    return len(Pasajeros) + 1


# -------- CREATE --------
def registro():
    print("\n--- Registro de pasajero ---")
    nuevo = []
    nuevo_id = getNewId()
    nuevo.append(nuevo_id)  # ID automático

    # Contraseña
    contraseña = input("Ingrese su Contraseña: ")
    nuevo.append(contraseña)

    # Mail (verificar unicidad)
    while True:
        mail = input("Ingrese su Mail: ")
        repetido = False
        for p in Pasajeros:
            if p[2] == mail:
                repetido = True
        if repetido:
            print("Ya existe un pasajero con ese mail.")
        else:
            nuevo.append(mail)
            break

    # DNI (verificar unicidad)
    while True:
        dni = input("Ingrese su DNI: ")
        repetido = False
        for p in Pasajeros:
            if p[3] == dni:
                repetido = True
        if repetido:
            print("Ya existe un pasajero con ese DNI.")
        else:
            nuevo.append(dni)
            break

    nombre = input("Ingrese su Nombre: ")
    nuevo.append(nombre)
    apellido = input("Ingrese su Apellido: ")
    nuevo.append(apellido)
    telefono = input("Ingrese su Teléfono: ")
    nuevo.append(telefono)
    fecha = input("Ingrese su Fecha de Nacimiento (AAAA-MM-DD): ")
    nuevo.append(fecha)

    Pasajeros.append(nuevo)
    print("Pasajero registrado con ID:", nuevo_id)
    return nuevo_id

# -------- READ (LOGIN) --------
def login():
    pid = 0
    bandera = False
    while bandera != False:
        while pid != 0:            
            print("\n--- Login ---")
            mail = input("Mail: ")
            if re.findall("@", mail) != 0:
                print("Mail no encontrado intente denuevo")
                break
            contraseña = input("Contraseña: ")
            for p in Pasajeros:
                if p[2] == mail and p[1] == contraseña:
                    print("✅ Bienvenido,", p[4], p[5])
                    pid = p[0]   # devolver ID
                    bandera = True
                    break
            print("Credenciales inválidas.")
    return pid




# -------- UPDATE --------
def actualizar():
    p = 0

# -------- DELETE --------
def eliminar():
    print("\n--- Eliminar pasajero ---")
    pid = input("Ingrese ID: ")
    for p in Pasajeros:
        if str(p[0]) == pid:
            Pasajeros.remove(p)
            print("Pasajero eliminado:", pid)
            return int(pid)
    print("No existe pasajero con ese ID.")
    return None

# -------- MENU --------
def menuPasajeros():
    idPasajero = 0
    salir = False
    
    while not salir:
        print("\n--- Menú Pasajeros ---")
        print("1. Registrar pasajero")
        print("2. Login")
        print("3. Actualizar pasajero")
        print("4. Eliminar pasajero")
        print("5. Salir")
        print()
        if(idPasajero != 0):
            print(f"usted ha iniciado sesion en la cuenta de {Pasajeros[pid][4]} {Pasajeros[pid][5]}")

        op = input("Opción: ")
        if op == "1":
            idPasajero = registro()
        elif op == "2":
            idPasajero = login()
        elif op == "3":
            actualizar(pid)
        elif op == "4":
            eliminar()
            idPasajero = 0
        elif op == "5":
            salir = True
        else:
            print("⚠️  Opción inválida.")

    return idPasajero

# ejecutar
