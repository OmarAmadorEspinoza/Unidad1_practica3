import json
import os

ARCHIVO_DATOS = "equipos_nba.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return []
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            if not datos: 
                return []
            return datos
    except json.JSONDecodeError:
        print("Error: El archivo JSON está corrupto. Se iniciará un inventario vacío.")
        return []

def guardar_datos(inventario):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, indent=4, ensure_ascii=False)