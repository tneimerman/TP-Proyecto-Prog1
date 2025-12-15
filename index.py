import CRUDs
from Helpers import *
if __name__ == "__main__":
    op = 0
    pasajero = traer_usuario()
    idp = int()
    print(pasajero)
    if pasajero != None:
        idp = pasajero[0]
    else:
        idp = 0
    bandera = True
    print("="*50)
    print("\033[1m Bienvenido al Sistema de Gestión de Vuelos\033[0m")
    
    while bandera:
        print("\n" + "="*50)
        print(" Elija una opcion:")
        if idp != 0:
            print(f" 1. Gestionar pasajeros\n 2. Gestionar aerolineas\n 3. Gestionar destinos\n 4. Gestionar vuelos\n 5. Gestionar vuelos de pasajeros\n 0. Salir")
        else:
            print("1. Gestionar pasajeros\n2. Gestionar aerolineas\n3. Gestionar destinos\n4. Gestionar vuelos"+"\033[9m \n5. Actualizar pasajero\033[0m" + "\n0. Salir")
        print("="*50)
        op = input("Opción: ")
        match op:
            case "1":
                CRUDs.menu_pasajeros()
            case "2":
                CRUDs.menu_aerolineas()
            case "3":
                CRUDs.menu_destinos()
            case "4":
                CRUDs.menu_vuelo()
            case "5":
                try:
                    if idp != 0:
                        CRUDs.menu_vuelo_pasajero()
                except:
                    raise PermissionError("Primero debes iniciar sesion para acceder a esta opcion")
            case "0":
                print("Gracias por usar el sistema!")
                borrar_usuario()
                bandera = False

            case _:
                print("Opción inválida.")