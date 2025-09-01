from data import referenciaPasajeros, Pasajeros

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
    print("✅ Pasajero registrado con ID:", nuevo_id)
    return nuevo_id

# -------- READ (LOGIN) --------
def login():
    print("\n--- Login ---")
    mail = input("Mail: ")
    contraseña = input("Contraseña: ")
    for p in Pasajeros:
        if p[2] == mail and p[1] == contraseña:
            print("✅ Bienvenido,", p[4], p[5])
            return p[0]   # devolver ID
    print("❌ Credenciales inválidas.")
    return None

# -------- READ (Buscar por DNI) --------
def buscar_por_dni():
    print("\n--- Buscar pasajero por DNI ---")
    dni = input("Ingrese DNI: ")
    for p in Pasajeros:
        if p[3] == dni:
            print("✅ Pasajero encontrado. ID:", p[0])
            for i in range(len(referenciaPasajeros)):
                print(referenciaPasajeros[i], ":", p[i])
            return p[0]
    print("❌ No existe pasajero con ese DNI.")
    return None

# -------- UPDATE --------
def actualizar():
    print("\n--- Actualizar pasajero ---")
    pid = input("Ingrese ID: ")
    encontrado = None
    for p in Pasajeros:
        if str(p[0]) == pid:
            encontrado = p
    if not encontrado:
        print("❌ No existe pasajero con ese ID.")
        return

    print("Deje vacío para no modificar.")
    for i in range(1, len(referenciaPasajeros)):
        actual = input(f"{referenciaPasajeros[i]} ({encontrado[i]}): ")
        if actual != "":
            encontrado[i] = actual
    print("✅ Actualización completa.")
    return int(pid)

# -------- DELETE --------
def eliminar():
    print("\n--- Eliminar pasajero ---")
    pid = input("Ingrese ID: ")
    for p in Pasajeros:
        if str(p[0]) == pid:
            Pasajeros.remove(p)
            print("🗑️  Pasajero eliminado:", pid)
            return int(pid)
    print("❌ No existe pasajero con ese ID.")
    return None

# -------- MENU --------
def menuPasajeros():
    salir = False
    
    while not salir:
        print("\n--- Menú Pasajeros ---")
        print("1. Registrar pasajero")
        print("2. Login")
        print("3. Buscar pasajero por DNI")
        print("4. Actualizar pasajero")
        print("5. Eliminar pasajero")
        print("6. Salir")

        op = input("Opción: ")
        if op == "1":
            registro()
        elif op == "2":
            login()
        elif op == "3":
            buscar_por_dni()
        elif op == "4":
            actualizar()
        elif op == "5":
            eliminar()
        elif op == "6":
            salir = True
        else:
            print("⚠️  Opción inválida.")

# ejecutar
id = 0
menuPasajeros()
