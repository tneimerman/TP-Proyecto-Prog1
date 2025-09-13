# CRUDs/Pasajeros.py
from data import referenciaPasajeros, Pasajeros
import re


def get_new_id():
    """ID autoincremental robusto (toma max + 1, no len)."""
    max_id = 0
    i = 0
    while i < len(Pasajeros):
        if Pasajeros[i][0] > max_id:
            max_id = Pasajeros[i][0]
        i += 1
    return max_id + 1

def buscar_idx_por_id(pid):
    i = 0
    while i < len(Pasajeros):
        if Pasajeros[i][0] == pid:
            return i
        i += 1
    return -1

def validar_mail(mail):

    if " " in mail:
        return False, "El mail no puede tener espacios."
    if re.search(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", mail) is None:
        return False, "Formato de mail inválido."
    return True, ""

def validar_dni(dni):
    if not dni.isdigit():
        return False, "El DNI debe ser solo dígitos."
    return True, ""

def validar_telefono(tel):
    if not tel.isdigit():
        return False, "El teléfono debe ser solo dígitos."
    return True, ""

def validar_fecha(fecha):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", fecha) is None:
        return False, "Formato de fecha inválido (use AAAA-MM-DD)."
    return True, ""

def registro():
    print("\n--- Registro de pasajero ---")
    nuevo = []
    nuevo_id = get_new_id()
    nuevo.append(nuevo_id)  # ID automático

    # Contraseña (mínimo: permitir cualquier string)
    contr = input("Ingrese su Contraseña: ")
    nuevo.append(contr)

    # Mail (solo formato)
    while True:
        mail = input("Ingrese su Mail: ")
        ok, msg = validar_mail(mail)
        if not ok:
            print("❌", msg)
            continue
        nuevo.append(mail)
        break

    # DNI (solo dígitos)
    while True:
        dni = input("Ingrese su DNI: ")
        ok, msg = validar_dni(dni)
        if not ok:
            print("❌", msg)
            continue
        nuevo.append(dni)
        break

    nombre = input("Ingrese su Nombre: ")
    nuevo.append(nombre)
    apellido = input("Ingrese su Apellido: ")
    nuevo.append(apellido)

    # Teléfono (solo dígitos)
    while True:
        tel = input("Ingrese su Teléfono: ")
        ok, msg = validar_telefono(tel)
        if not ok:
            print("❌", msg)
            continue
        nuevo.append(tel)
        break

    # Fecha Nacimiento (patrón simple)
    while True:
        fecha = input("Ingrese su Fecha de Nacimiento (AAAA-MM-DD): ")
        ok, msg = validar_fecha(fecha)
        if not ok:
            print("❌", msg)
            continue
        nuevo.append(fecha)
        break

    Pasajeros.append(nuevo)
    print("✅ Pasajero registrado con ID:", nuevo_id)
    return nuevo_id


def login():

    print("\n--- Login --- (o escriba 'q' para salir)")
    while True:
        mail = input("Mail: ")
        if mail.lower() == "q":
            return 0

        ok, msg = validar_mail(mail)
        if not ok:
            print("❌", msg)
            continue

        contr = input("Contraseña: ")
        if contr.lower() == "q":
            return 0

        # Buscar coincidencia exacta mail/contraseña
        i = 0
        while i < len(Pasajeros):
            if Pasajeros[i][2] == mail and Pasajeros[i][1] == contr:
                print(f"✅ Bienvenido, {Pasajeros[i][4]} {Pasajeros[i][5]}")
                return Pasajeros[i][0]
            i += 1

        print("❌ Credenciales inválidas.")


def actualizar(pid=None):
    print("\n--- Actualizar pasajero ---")
    if pid is None:
        entrada = input("Ingrese ID a actualizar: ")
        if not entrada.isdigit():
            print("❌ ID inválido.")
            return None
        pid = int(entrada)

    idx = buscar_idx_por_id(pid)
    if idx == -1:
        print("❌ No existe pasajero con ese ID.")
        return None

    p = Pasajeros[idx]
    print("Editando a:", p)


    nuevo = input(f"Contraseña [{p[1]}]: ")
    if nuevo != "":
        p[1] = nuevo


    while True:
        nuevo = input(f"Mail [{p[2]}]: ")
        if nuevo == "":
            break
        ok, msg = validar_mail(nuevo)
        if ok:
            p[2] = nuevo
            break
        print("❌", msg)


    while True:
        nuevo = input(f"DNI [{p[3]}]: ")
        if nuevo == "":
            break
        ok, msg = validar_dni(nuevo)
        if ok:
            p[3] = nuevo
            break
        print("❌", msg)

    # Nombre    nuevo = input(f"Nombre [{p[4]}]: ")
    if nuevo != "":
        p[4] = nuevo


    nuevo = input(f"Apellido [{p[5]}]: ")
    if nuevo != "":
        p[5] = nuevo


    while True:
        nuevo = input(f"Teléfono [{p[6]}]: ")
        if nuevo == "":
            break
        ok, msg = validar_telefono(nuevo)
        if ok:
            p[6] = nuevo
            break
        print("❌", msg)

    while True:
        nuevo = input(f"Fecha Nacimiento [{p[7]}] (AAAA-MM-DD): ")
        if nuevo == "":
            break
        ok, msg = validar_fecha(nuevo)
        if ok:
            p[7] = nuevo
            break
        print("❌", msg)

    print("✅ Pasajero actualizado.")
    return pid


def eliminar():
    """
    Elimina pasajero por ID. Borrado por coincidencia exacta del ID.
    """
    print("\n--- Eliminar pasajero ---")
    entrada = input("Ingrese ID: ")
    if not entrada.isdigit():
        print("❌ ID inválido.")
        return None
    pid = int(entrada)

    idx = buscar_idx_por_id(pid)
    if idx == -1:
        print("❌ No existe pasajero con ese ID.")
        return None

    Pasajeros.pop(idx)
    print("🗑️ Pasajero eliminado:", pid)
    return pid



def menu_pasajeros():
    id_pasajero = 0
    salir = False

    while not salir:
        print("\n--- Menú Pasajeros ---")
        print("1. Registrar pasajero")
        print("2. Login")
        print("3. Actualizar pasajero")
        print("4. Eliminar pasajero")
        print("5. Salir")
        if id_pasajero != 0:
            idx = buscar_idx_por_id(id_pasajero)
            if idx != -1:
                print(f"\nSesión iniciada: {Pasajeros[idx][4]} {Pasajeros[idx][5]} (ID {id_pasajero})")

        op = input("\nOpción: ").strip()
        match op:
            case "1":
                id_pasajero = registro()
            case "2":
                id_pasajero = login()
            case "3":
                actualizar()  # pide ID adentro
            case "4":
                eliminado = eliminar()
                if eliminado == id_pasajero:
                    id_pasajero = 0
            case "5":
                break
            case _:
                print("⚠️  Opción inválida.")
                continue
    return id_pasajero
