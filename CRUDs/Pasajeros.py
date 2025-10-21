# CRUDs/Pasajeros.py
from data import referenciaPasajeros, Pasajeros
from CRUDs.Validaciones import validar_dni,validar_fecha,validar_mail,validar_telefono
def displayActualizar():
    start = referenciaPasajeros.index("Contraseña")
    for i, campo in enumerate(referenciaPasajeros[start:], start=start):
        print(f"{i}. {campo}")
    print("8. Todo")
    op = input()
    return op
def getPosMatriz():
    contra = referenciaPasajeros.index("Contraseña")
    mail = referenciaPasajeros.index("Mail")
    dni = referenciaPasajeros.index("DNI")
    nombre = referenciaPasajeros.index("Nombre")
    apellido = referenciaPasajeros.index("Apellido")
    telefono = referenciaPasajeros.index("Telefono")
    fecha = referenciaPasajeros.index("Fecha Nacimiento")
    return contra, mail, dni, nombre, apellido, telefono, fecha
def funcionActualizar(op,idp):
    idPasajero = idp - 1
    contra, mail, dni, nombre, apellido, telefono, fecha = getPosMatriz()
    valid_mail, valid_DNI, valid_tel, valid_fecha = False, False, False, False
    match op:
        case "1":
            print("Inserte la nueva contraseña:")
            nuevaContra = input()
            Pasajeros[idPasajero][contra] = nuevaContra
            return True
        case "2":
            while True:
                try:
                    print("Inserte el nuevo mail:")
                    nuevoMail = input()
                    valid_mail = validar_mail(nuevoMail)
                    Pasajeros[idPasajero][mail] = nuevoMail
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
                    Pasajeros[idPasajero][dni] = nuevoDNI
                    break
                except ValueError:
                    print("DNI invalido, intente denuevo")
                    continue
        case "4":
            print("Inserte el nuevo nombre:")
            nuevoNombre = input()
            Pasajeros[idPasajero][nombre] = nuevoNombre
            return True
        case "5":
            print("Inserte el nuevo apellido:")
            nuevoApellido = input()
            Pasajeros[idPasajero][apellido] = nuevoApellido
            return True
        case "6":
            while True:
                try:
                    print("Inserte el nuevo telefono:")
                    nuevoTelefono = input()
                    valid_tel  = validar_telefono(nuevoTelefono)
                    Pasajeros[idPasajero][telefono] = nuevoTelefono
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
                    Pasajeros[idPasajero][fecha] = nuevaFecha
                    break
                except ValueError:
                    print("Fecha invalida, intente denuevo")
                    continue
        case _:
            print("Opcion invalida")
        

def buscarPasajero(dato):
    for x in Pasajeros:
        for y in x:
            if y == dato:
                return x
        

      
def get_new_id():
    return len(Pasajeros)+1



def datos_pasajero(id_pasajero):
    print("="*28)
    print(f"Datos del pasajero")
    print("="*28)
    
    print(f"╔{"="*28}╗")
    if id_pasajero == 0:
        print("Inicie sesión para ver sus datos.")
    for i in range(len(Pasajeros[id_pasajero])):
        print(f"║{referenciaPasajeros[i]}: {Pasajeros[id_pasajero][i]}\n║{" "*28}║")
    print(f"╚{"="*28}╝")
        

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
        if ok != True:
            print(msg)
            continue
        nuevo.append(mail)
        break

    # DNI (solo dígitos)
    while True:
        dni = input("Ingrese su DNI: ")
        ok, msg = validar_dni(dni)
        if ok != True:
            print( msg)
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
        if  ok != True:
            print( msg)
            continue
        nuevo.append(tel)
        break

    # Fecha Nacimiento (patrón simple)
    while True:
        fecha = input("Ingrese su Fecha de Nacimiento (AAAA-MM-DD): ")
        ok, msg = validar_fecha(fecha)
        if ok != True:
            print( msg)
            continue
        nuevo.append(fecha)
        break

    Pasajeros.append(nuevo)
    print("Pasajero registrado con ID:", nuevo_id)
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
                print(f"Bienvenido, {Pasajeros[i][4]} {Pasajeros[i][5]}")
                return Pasajeros[i][0]
            i += 1

        print("Credenciales inválidas.")



def actualizar(id_pasajero):
    op = 0
    bandera = False
    print("="*50)
    print("\n--- Actualizar pasajero ---")
    print("="*50)
    while bandera != True:
        print("Elige una opcion:")
        op = displayActualizar()
        bandera = funcionActualizar(op, id_pasajero)
        
    print("Pasajero actualizado exitosamente")



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