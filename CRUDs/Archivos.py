from Helpers import fix_info
def get_info_by_id(id, archivo):
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

def print_info(archivo):
    try:
        arch = open(archivo, "r", encoding="UTF-8")
        for linea in arch:
            lista = fix_info(linea)
            for x in lista:
                print(f"{x:>10}")   
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")

def save_data(matriz, archivo):
    try:
        # Convertimos cada fila a string con punto y coma y salto de línea
        lineas = [f"{x};" for x in matriz]
        lineas = lineas[-1].replace(";", "\n")  # Última línea sin ;
        arch = open(archivo, "wt")
        arch.writelines(lineas)
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
            print(f'Archivo {archivo} creado con éxito')
        except NameError:
            pass