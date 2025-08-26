from data import Pasajeros
from data import referenciaPasajeros
posUser = referenciaPasajeros.index("ID")
posContraseña = referenciaPasajeros.index("Contraseña")
    

def Registro():
    listaAgregado = []
    for i in range(len(referenciaPasajeros)):
        dataInsert = input(f"Ingrese su {referenciaPasajeros[i]}: ")
        listaAgregado.append(dataInsert)
    Pasajeros.append(listaAgregado)

def Login():
    success = False
    while success != True:
        usuario = input("Ingrese el nombre de usuario")
        contraseña = input("Ingrese la contraseña")
        
        

          
def MenuLog():
    success = False
    while success != True:
        print(f"╔{"═":═^18}╗")
        print(f"║ {"Elije una opcion":^1} ║")
        print(f"║ 1. Registro      ║")
        print(f"║ 2. Inicio sesion ║")
        print(f"║ 3. Salir         ║")
        print(f"╚{"═":═^17}═╝")
        ans = int(input(""))
        match ans:
            case 1:
                Registro()
                success = True
            case 2:
                Login()
                success = True
            case 3:
                success = True
            case _:
                success = False



MenuLog()