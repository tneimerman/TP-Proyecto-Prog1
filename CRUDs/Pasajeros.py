# CRUDs/Pasajeros.py
from data import referenciaPasajeros, Pasajeros
import re
def validar_mail(mail):

    if re.search(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", mail) == None:
        return False, "Formato de mail inválido."
    return True, ""

def validar_dni(dni):
    if  dni.isdigit() == False:
        return False, "El DNI debe ser solo dígitos."
    return True, ""

def validar_telefono(tel):
    if tel.isdigit() == False:
        return False, "El teléfono debe ser solo dígitos."
    return True, ""

def validar_fecha(fecha):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", fecha) is None:
        return False, "Formato de fecha inválido (use AAAA-MM-DD)."
    return True, ""
def displayActualizar():
    start = referenciaPasajeros.index("Contraseña")
    for i, campo in enumerate(referenciaPasajeros[start:], start=start):
        print(i, campo)
    print("7. Todo")
def getPosMatriz():
    contra = referenciaPasajeros.index("Contraseña")
    mail = referenciaPasajeros.index("Mail")
    dni = referenciaPasajeros.index("DNI")
    nombre = referenciaPasajeros.index("Nombre")
    apellido = referenciaPasajeros.index("Apellido")
    telefono = referenciaPasajeros.index("Telefono")
    fecha = referenciaPasajeros.index("Fecha Nacimiento")
    return contra, mail, dni, nombre, apellido, telefono, fecha
def funcionActualizar(op,idPasajero):
    contra, mail, dni, nombre, apellido, telefono, fecha = getPosMatriz()
    valid_mail, valid_DNI, valid_tel, valid_fecha = False
    match op:
        case "1":
            print("Inserte la nueva contraseña:")
            nuevaContra = input()
            Pasajeros[idPasajero][contra] = nuevaContra
        case "2":
            while valid_mail == False:
                print("Inserte el nuevo mail:")
                nuevoMail = input()
                valid_mail, msg = validar_mail(nuevoMail)
                if valid_mail == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][mail] = nuevoMail
        case "3":
            while valid_DNI == False:
                print("Inserte el nuevo DNI:")
                nuevoDNI = input()
                valid_DNI, msg = validar_dni(nuevoDNI)
                if valid_DNI == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][dni] = nuevoDNI
        case "4":
            print("Inserte el nuevo nombre:")
            nuevoNombre = input()
            Pasajeros[idPasajero][nombre] = nuevoNombre
        case "5":
            print("Inserte el nuevo apellido:")
            nuevoApellido = input()
            Pasajeros[idPasajero][apellido] = nuevoApellido
        case "6":
            while valid_tel == False:
                print("Inserte el nuevo telefono:")
                nuevoTelefono = input()
                valid_tel, msg = validar_telefono(nuevoTelefono)
                if valid_tel == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][telefono] = nuevoTelefono
        case "7":
            while valid_fecha == False:
                print("Inserte la nueva fecha de nacimiento:")
                nuevaFecha = input()
                valid_fecha, msg = validar_fecha(nuevaFecha)
                if valid_fecha == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][fecha] = nuevaFecha
        case "8": 
            print("Inserte la nueva contraseña:")
            nuevaContra = input()
            Pasajeros[idPasajero][contra] = nuevaContra
            while valid_mail == False:
                print("Inserte el nuevo mail:")
                nuevoMail = input()
                valid_mail, msg = validar_mail(nuevoMail)
                if valid_mail == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][mail] = nuevoMail
            while valid_DNI == False:
                print("Inserte el nuevo DNI:")
                nuevoDNI = input()
                valid_DNI, msg = validar_dni(nuevoDNI)
                if valid_DNI == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][dni] = nuevoDNI
            print("Inserte el nuevo nombre:")
            nuevoNombre = input()
            Pasajeros[idPasajero][nombre] = nuevoNombre
            print("Inserte el nuevo apellido:")
            nuevoApellido = input()
            Pasajeros[idPasajero][apellido] = nuevoApellido
            while valid_tel == False:
                print("Inserte el nuevo telefono:")
                nuevoTelefono = input()
                valid_tel, msg = validar_telefono(nuevoTelefono)
                if valid_tel == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][telefono] = nuevoTelefono
            while valid_fecha == False:
                print("Inserte la nueva fecha de nacimiento:")
                nuevaFecha = input()
                valid_fecha, msg = validar_fecha(nuevaFecha)
                if valid_fecha == False:
                    print(msg)
                else:
                    Pasajeros[idPasajero][fecha] = nuevaFecha
        

def buscarPasajero(dato):
    for i in range(len(Pasajeros)):
        x = i
        for j in range(len(Pasajeros[i])):
            if Pasajeros[i][j] == dato:
                return x

      
def get_new_id():
    """ID autoincremental robusto (toma max + 1, no len)."""
    max_id = 0
    i = 0
    while i < len(Pasajeros):
        if Pasajeros[i][0] > max_id:
            max_id = Pasajeros[i][0]
        i += 1
    return max_id + 1





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

    print("\n--- Login ---")
    while True:
        mail = input("Mail: ")

        ok, msg = validar_mail(mail)
        if ok == False:
            print( msg)
            continue

        contr = input("Contraseña: ")

        # Buscar coincidencia exacta mail/contraseña
        i = 0
        while i < len(Pasajeros):
            if Pasajeros[i][2] == mail and Pasajeros[i][1] == contr:
                print(f"✅ Bienvenido, {Pasajeros[i][4]} {Pasajeros[i][5]}")
                return Pasajeros[i][0]
            i += 1

        print("Credenciales inválidas.")



def actualizar():
    op = 0
    print("="*50)
    print("\n--- Actualizar pasajero ---")
    print("="*50)

    print("Elige una opcion:")
    op = displayActualizar()
    funcionActualizar(op)



def eliminar():
    print("="*50)
    print("\n--- Eliminar pasajero ---")
    print("="*50)
    entrada = input("Ingrese cualquier dato del pasajero: ")
    x = buscarPasajero(entrada)
    if x is None:
        print("No se encontro el pasajero con ese dato")
    else:
        sn = input(f"Esta seguro de eliminar el pasajero {Pasajeros[x][4]} {Pasajeros[x][5]}? (s/n): ")
        if sn.lower() == "s":
        
            Pasajeros.pop(x)
            print("Pasajero eliminado exitosamente")
    



def menu_pasajeros():
    salir = False
    id_pasajero = int()
    while salir != True:
        print()
        print("="*50)
        print("\n--- Menú Pasajeros ---")
        print("="*50)
        print("1. Registrar pasajero")
        print("2. Login")
        if id_pasajero != 0:
            print("3. Actualizar pasajero")
            print("4. Eliminar pasajero")
        else:
            print("\033[9m3. Actualizar pasajero\033[0m")
            print("\033[9m4. Eliminar pasajero\033[0m")
            print("Inicie sesion o registrese para acceder a estas opciones")            
        print("0. Salir")
        print("="*50)
        if id_pasajero != 0:
            print(f"\nSesión iniciada: {Pasajeros[id_pasajero-1][4]} {Pasajeros[id_pasajero-1][5]} (ID {id_pasajero})")

        op = input("\nOpción: ").strip()
        match op:
            case "1":
                id_pasajero = registro()
            case "2":
                id_pasajero = login()
            case "3":
                actualizar()  # pide ID adentro
            case "4":
                eliminar()

            case "0":
                print("Volviendo al menú...")
                salir = True
            case _:
                print("⚠️  Opción inválida.")
    return id_pasajero

