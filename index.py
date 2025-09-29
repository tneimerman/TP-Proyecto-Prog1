import CRUDs

if __name__ == "__main__":
    op = 0
    idp = 0
    bandera = True
    print("="*50)
    print("\033[1m Bienvenido al Sistema de Gestión de Vuelos\033[0m")
    
    while bandera:
        print("\n" + "="*50)
        print(" Elija una opcion:")
        print(" 1. Gestionar pasajeros\n 2. Gestionar aerolineas\n 3. Gestionar destinos\n 4. Gestionar vuelos\n 5. Gestionar vuelos de pasajeros\n 0. Salir")
        print("="*50)
        op = input("Opción: ")
        match op:
            case "1":
                idp = CRUDs.menu_pasajeros(idp)
            case "2":
                CRUDs.menu_aerolineas()
            case "3":
                CRUDs.menu_destinos()
            case "4":
                CRUDs.menu_vuelo()
            case "5":
                
                CRUDs.menu_vuelo_pasajero()  
            case "0":
                print("Gracias por usar el sistema!")
                bandera = False
            case _:
                print("Opción inválida.")