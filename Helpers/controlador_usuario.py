from Helpers.Archivos import fix_info
archivo = 'Archivos/User.txt'
def guardar_usuario(user):
    try:
        if user != None:
            linea_fixed = ';'.join(str(x) for x in user) + '\n'
            arch = open(archivo, "wt", encoding="UTF-8")
            arch.write(linea_fixed)        
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
def traer_usuario():
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        if arch != "":
            for linea in arch:
                lista = fix_info(linea)
                for i in lista:
                    if i.isdigit() == True:
                        count = lista.index(i)
                        lista[count] = int(i)
                return lista
    except OSError as mensaje:
        print("No se pudo traer el usuario:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
def borrar_usuario():
    try:
        arch = open(archivo, "wt", encoding="UTF-8")
        arch.write("")
    except OSError as mensaje:
        print("No se pudo traer el usuario:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass