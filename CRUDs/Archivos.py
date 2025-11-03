import os

def fix_info(l):
    list = l.split(";")
    list[-1] = list[-1].strip("\n")
    return list

def get_max_id(archivo):
    try:
        count = 0
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            count += 1
        return count + 1
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo") 

def get_lista_by_dato(dato, archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            if str(dato) in lista:
                return lista      
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def print_info(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            for x in lista:
                print(f"║{x:^20}", end="")
            print()
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def save_data(matriz, archivo):
    try:
        arch = open(archivo, "a", encoding="UTF-8")
        linea_fixed = ';'.join(str(x) for x in matriz) + '\n'
        arch.write(linea_fixed) 
        print("Agregado correctamente:", matriz)
        
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
def delete_data(archivo, id, list):
    temp = "temp.txt"
    encontrado = False

    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")
        new_linea = (";".join(str(x) for x in list) + "\n")
        for linea in arch:
            datos = linea.strip().split(";")
            codigo = datos[0]
            if codigo != str(id):
                aux.write(linea)
            else:
                aux.write(new_linea)
                encontrado = True

    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove(archivo)       # elimina el original
            os.rename(temp, archivo) # renombra el temporal
            print(f"Linea con el id: {id} eliminado correctamente.")
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)  # eliminamos el temporal si no se usó
        print(f"No se encontró el id: {id}.")
