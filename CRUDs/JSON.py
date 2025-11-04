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