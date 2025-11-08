import os

def fix_info(l):
    list = l.split(";")
    list[-1] = list[-1].strip("\n")
    return list
def obtener_matriz(archivo):
    lista = []
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista_aux = fix_info(linea)
            lista.append(lista_aux)
        return lista
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo") 


def obtener_lista_por_dato(dato, archivo):
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
def obtener_lista_por_id(id, archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            if str(id) == lista[0]:
                return lista      
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def mostrar_informacion(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            for x in lista:
                print(f"║{x:^15 if len[x] > 15 else x:>15}", end="")
            print()
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def guardar_data(archivo, matriz):
    try:
        linea_fixed = ';'.join(str(x) for x in matriz) + '\n'
        arch = open(archivo, "a", encoding="UTF-8")
        arch.write(linea_fixed) 
        print("Agregado correctamente:", matriz)
        
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass
def borrar_data(archivo, id, list):
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
def modificar_lista(archivo, new_dato, pos_dato, id):
    temp = "temp.txt"
    encontrado = False
    anterior = None
    lista_aux = []
    try:
        arch = open(archivo, "rt", encoding="UTF-8")
        aux = open(temp, "wt", encoding="UTF-8")
        for linea in arch:
            datos = fix_info(linea)
            if str(id) == datos[0]:
                anterior = datos[int(pos_dato)]
                lista_aux = datos
                lista_aux[int(pos_dato)] = new_dato
                linea_fixed = ';'.join(str(x) for x in lista_aux) + '\n'
                aux.write(linea_fixed)
                encontrado = True
                
            else:
                linea_fixed = ';'.join(str(x) for x in datos) + '\n'
                aux.write(linea_fixed) 
    except FileNotFoundError:
        print("El archivo no existe.")
    except OSError as error:
        print("Error en el acceso al archivo:", error)
    finally:
        try:
            arch.close()
            aux.close()
            print(f"Dato modificado de '{anterior}' a '{new_dato}' correctamente.")
        except:
            print("Error en el cierre del archivo:")

    if encontrado:
        try:
            os.remove(archivo)
            os.rename(temp, archivo)
        except OSError as error:
            print("Error al reemplazar el archivo:", error)
    else:
        os.remove(temp)
        print(f"No se encontró el producto.")