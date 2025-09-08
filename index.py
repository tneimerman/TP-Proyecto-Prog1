import CRUDs

if __name__ == "__main__":
    op = 0
    while True:
        print("\033[1mBienvenido al sistema de gestión de pasajeros\033[0m")
        print("Elija una opcion:")
        print("1. Gestionar pasajeros")
        print("2. Gestionar aerolineas")
        op = input("\nOpción: ")
        match op:
            case "1":
                idp = CRUDs.menu_pasajeros()
            case "2":
                CRUDs.menu_aerolineas()

