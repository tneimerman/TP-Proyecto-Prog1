from data import Pasajeros, Vuelos, Destinos, Aerolinea, vuelo_pasajero
import json
def cargar_matriz_en_archivo(matriz, archivo):
    try:
        # Convertimos cada fila a string con punto y coma y salto de línea
        lineas = [";".join(map(str, x)) + "\n" for x in matriz]
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

try:
    archivo = open("Archivos/VuelosPasajero.json", "w")
    json.dump(vuelo_pasajero, archivo)
except OSError as mensaje:
    print("No se puede abrir el archivo:", mensaje)
finally:
    archivo.close()