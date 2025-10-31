# CRUDs/Pasajeros.py
from data import referenciaPasajeros, Pasajeros
from CRUDs.Archivos import *
from Helpers import * 
archivo_modulo = "Archivos/Pasajeros.txt"

def show_list(list):
    if len(list) > 1:
        print(f"{referenciaPasajeros.index(list[1])}. {list[1]}")
        show_list(list[1:])
def displayActualizar():
    print("Seleccione una opcion para actualizar")
    show_list(referenciaPasajeros)
    op = input()
    return op
def funcionActualizar(op,idp):
    idPasajero = idp - 1
    pasajero = get_info_by_id(idPasajero, archivo_modulo)
    op = displayActualizar()
    match op:
        case "1":
            print("Inserte la nueva contraseña:")
            nuevaContra = input()
            pasajero[op] = nuevaContra
            return True
        case "2":
            while True:
                try:
                    print("Inserte el nuevo mail:")
                    nuevoMail = input()
                    valid_mail = validar_mail(nuevoMail)
                    pasajero[op] = nuevoMail
                    break
                except ValueError:
                    print("Mail invalido, intente devuelta")
                    continue
        case "3":
            while True:
                try:
                    print("Inserte el nuevo DNI:")
                    nuevoDNI = input()
                    valid_DNI = validar_dni(nuevoDNI)
                    pasajero[op] = nuevoDNI
                    break
                except ValueError:
                    print("DNI invalido, intente denuevo")
                    continue
        case "4":
            print("Inserte el nuevo nombre:")
            nuevoNombre = input()
            pasajero[op] = nuevoNombre
            return True
        case "5":
            print("Inserte el nuevo apellido:")
            nuevoApellido = input()
            pasajero[op] = nuevoApellido
            return True
        case "6":
            while True:
                try:
                    print("Inserte el nuevo telefono:")
                    nuevoTelefono = input()
                    valid_tel  = validar_telefono(nuevoTelefono)
                    pasajero[op] = nuevoTelefono
                    break
                except ValueError:
                    print("Telefono invalido, intente denuevo")
                    continue
                    
        case "7":
            while True:
                try:
                    print("Inserte la nueva fecha de nacimiento:")
                    nuevaFecha = input()
                    valid_fecha = validar_fecha(nuevaFecha)
                    pasajero[op] = nuevaFecha
                    break
                except ValueError:
                    print("Fecha invalida, intente denuevo")
                    continue
        case _:
            print("Opcion invalida")
    
        
def buscarPasajero(dato):
    for x in Pasajeros:
        if dato in x:
            return x
        
def get_new_id():
    return len(Pasajeros)+1



def datos_pasajero(id_pasajero):
    lista = get_info_by_id(id_pasajero, archivo_modulo)
    referencia = f"║{referenciaPasajeros[0]:<5} {referenciaPasajeros[1]:<15} {referenciaPasajeros[2]:<20} {referenciaPasajeros[3]:<20} {referenciaPasajeros[4]:<15} {referenciaPasajeros[5]:<15} {referenciaPasajeros[6]:<15} {referenciaPasajeros[7]:<20}   ║"
    print("="*(len(referencia)-2))
    print(f"Datos del pasajero")
    print("="*(len(referencia)-2))
    print(f"╔{"═"*(len(referencia)-2)}╗")
    print(referencia)
    print(f"╠{"═"*(len(referencia)-2)}╣")
    print(f"║{lista[0]:<5} {lista[1]:<15} {lista[2]:<20} {lista[3]:<20} {lista[4]:<15} {lista[5]:<15} {lista[6]:<15} {lista[7]:<20}   ║")
    print(f"╚{"═"*(len(referencia)-2)}╝")

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
        try:
            print("Inserte el nuevo mail:")
            nuevoMail = input()
            valid_mail = validar_mail(nuevoMail)
            nuevo.append(valid_mail)
            break
        except ValueError:
                print("Mail invalido, intente devuelta")
                continue

    # DNI (solo dígitos)
    while True:
        try:
            print("Inserte el nuevo DNI:")
            nuevoDNI = input()
            valid_DNI = validar_dni(nuevoDNI)
            nuevo.append(valid_DNI)
            break
        except ValueError:
            print("DNI invalido, intente denuevo")
            continue

    nombre = input("Ingrese su Nombre: ")
    nuevo.append(nombre)
    apellido = input("Ingrese su Apellido: ")
    nuevo.append(apellido)

    # Teléfono (solo dígitos)
    while True:
        try:
            print("Inserte el nuevo telefono:")
            nuevoTelefono = input()
            valid_tel  = validar_telefono(nuevoTelefono)
            nuevo.append(valid_tel)
            break
        except ValueError:
            print("Telefono invalido, intente denuevo")
            continue
                    

    # Fecha Nacimiento (patrón simple)
    while True:
        try:
            print("Inserte la nueva fecha de nacimiento:")
            nuevaFecha = input()
            valid_fecha = validar_fecha(nuevaFecha)
            nuevo.append(valid_fecha)
            break
        except ValueError:
            print("Fecha invalida, intente denuevo")
            continue

    save_data(archivo_modulo, nuevo)
    print("Pasajero registrado con ID:", nuevo_id)
    return nuevo_id


def login():

    print("\n--- Login ---")
    while True:
        while True:
            try:
                mail = input("Mail: ")
                valid_mail = validar_mail(mail)
                break
            except ValueError:
                print("Mail invalido, intente devuelta")
                continue

        contr = input("Contraseña: ")

        # Buscar coincidencia exacta mail/contraseña
        i = 0
        while i < len(Pasajeros):
            if Pasajeros[i][2] == mail and Pasajeros[i][1] == contr:
                print(f"Bienvenido, {Pasajeros[i][4]} {Pasajeros[i][5]}")
                return Pasajeros[i][0]
            i += 1

        print("Credenciales inválidas.")



def actualizar(id_pasajero):
    op = 0
    print("="*50)
    print("\n--- Actualizar pasajero ---")
    print("="*50)
    while True:
        try:
            print("Elige una opcion:")
            op = displayActualizar()
            bandera = funcionActualizar(op, id_pasajero)
            print("Pasajero actualizado exitosamente")
            break
        except ValueError:
            print("Opcion invalida intente devuelta")
            continue

        
    



def eliminar(id_pasajero):
    print("="*50)
    print("\n--- Eliminar pasajero ---")
    print("="*50)
    sn = input(f"Esta seguro de eliminar el pasajero {Pasajeros[id_pasajero][4]} {Pasajeros[id_pasajero][5]}? (s/n): ")
    if sn.lower() == "s":
        Pasajeros.pop(id_pasajero)
        print("Pasajero eliminado exitosamente")
    



def menu_pasajeros(id_pasajero=0):
    salir = False
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
            print("5. Mostrar datos del pasajero")
        else:

            print("\033[9m3. Actualizar pasajero\033[0m")
            print("\033[9m4. Eliminar pasajero\033[0m")
            print("\033[9m5. Mostrar datos del pasajero\033[0m")
            print("Inicie sesion o registrese para acceder a estas opciones")            
        print("0. Salir")
        print("="*50)

        if id_pasajero != 0:
            try:
                print(f"\nSesión iniciada: {Pasajeros[id_pasajero-1][4]} {Pasajeros[id_pasajero-1][5]} (ID {id_pasajero})")
            except Exception:

                print(f"\nSesión iniciada con ID {id_pasajero} (registro no disponible)")

        op = input("\nOpción: ").strip()
        match op:
            case "1":

                id_pasajero = registro()
            case "2":

                id_pasajero = login()
            case "3":
                try:
                    if id_pasajero != 0:
                        actualizar(id_pasajero)
                except PermissionError:
                    print("Primero inicie sesion para acceder a esta opcion", PermissionError)
            case "4":
                try:
                    if id_pasajero != 0:
                        eliminar(id_pasajero)
                except PermissionError:
                    print("Primero inicie sesion para acceder a esta opcion", PermissionError)
            case "5":
                try:
                    if id_pasajero != 0:
                        datos_pasajero(id_pasajero)
                except PermissionError:
                    print("Primero inicie sesion para acceder a esta opcion", PermissionError)
            case "0":
                print("Volviendo al menú...")
                salir = True
            case _:
                print("Opción inválida.")
    return id_pasajero