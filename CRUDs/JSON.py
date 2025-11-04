import os
import json

archivo_modulo = "Archivos/VuelosPasajero.json"

def obtener_diccionarios():
    try:
        arch = open(archivo_modulo, "r")
        json_string = json.load(arch)
        return json_string
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")
def obtener_diccionario_por_id(id):
    try:
        arch = open(archivo_modulo, "r")
        json_string = json.load(arch)
        for dic in json_string:
            if dic["ID"] == id:
                return dic
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")
def guardar_diccionario(dic):
    try:
        with open(archivo_modulo, "r", encoding="UTF-8") as arch:
            dict = json.load(arch)
        dict.append(dic)
        with open(archivo_modulo, "w", encoding="UTF-8") as arch:
            json.dump(dict, arch, ensure_ascii=False)
    except (FileNotFoundError,OSError) as error:
        print(f"Error {error}")
def eliminar_diccionario(id):
    try:
        with open(archivo_modulo, "r", encoding="UTF-8") as arch:
            dict = json.load(arch)
        ids = [dic["ID"] for dic in dict]
        if id in ids:
            indice = ids.index(id)
            dict.pop(indice)
            with open(archivo_modulo, "w", encoding="UTF-8") as arch:
                dict = json.dump(dict, arch, ensure_ascii=False)           
            print(f"No se encontro la referencia con el id: {id}")
        
        
    except (FileNotFoundError,OSError) as error:
        print(f"Error {error}")
def modificar_diccionario(dato_nuevo, pos, id):
    try:
        with open(archivo_modulo, "r", encoding="UTF-8") as arch:
            dict = json.load(arch)
        ids = [dic["ID"] for dic in dict]
        if id in ids:
            indice = ids.index(id)
            dict[indice][f"{pos}"] = dato_nuevo
            with open(archivo_modulo, "w", encoding="UTF-8") as arch:
                dict = json.dump(dict, arch, ensure_ascii=False)
            
            print(f"No se encontro la referencia con el id: {id}")
        
        
    except (FileNotFoundError,OSError) as error:
        print(f"Error {error}")
    