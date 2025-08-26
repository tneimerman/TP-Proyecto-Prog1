from data import Usuarios
from data import referenciaUsuarios
posUser = referenciaUsuarios.index("Usuario")
posContraseña = referenciaUsuarios.index("Contraseña")
    

def Registro():
    listaAgregado = []
    for i in range(len(referenciaUsuarios)):
        dataInsert = input(f"Ingrese su {referenciaUsuarios[i]}: ")
        listaAgregado.append(dataInsert)
    Usuarios.append(listaAgregado)

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