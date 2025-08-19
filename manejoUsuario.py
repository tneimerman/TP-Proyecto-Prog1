from data import Usuarios
from data import referenciaUsuarios
posUser = referenciaUsuarios.index("Usuario")
posContraseña = referenciaUsuarios.index("Contraseña")
def Busqueda(item):
    

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
        print("╔══════════════════╗")
        print("║ Elije una opcion ║")
        print("║ 1. Registro      ║")
        print("║ 2. Inicio sesion ║")
        print("║ 3. Salir         ║")
        print("╚══════════════════╝")
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