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

        print(" Credenciales inválidas.")


def actualizar(pid):
    correct = False
    print(f"\n{"Actualizar pasajero":-3}")
    print(f"Bienvenido {Pasajeros[pid][4]} {Pasajeros[pid][5]}")
    print("¿Que desea actualizar\n1.")
    




def eliminar(pid):

    print(f"\n{"Eliminar pasajero":-3}")
    print(f"¿Desea eliminar el pasajero {Pasajeros[pid][4], Pasajeros[pid][5]}")
    op = input("s/n ")
    if op.lower() == "s":
        Pasajeros.pop(pid)
        print("Pasajero eliminado correctamente")
    else:
        print()



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
            print(f"\nSesión iniciada: {Pasajeros[id_pasajero][4]} {Pasajeros[id_pasajero][5]} (ID {id_pasajero})")

        op = input("\nOpción: ").strip()
        match op:
            case "1":
                id_pasajero = registro()
            case "2":
                id_pasajero = login()
            case "3":
                actualizar(id_pasajero)  # pide ID adentro
            case "4":
                eliminado = eliminar()
                if eliminado == id_pasajero:
                    id_pasajero = 0
            case "5":
                salir = True
            case _:
                print("Opción inválida.")
                
    return id_pasajero
