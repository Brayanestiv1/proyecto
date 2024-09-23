import os
import json

def registrar_grupo():
    codigo = input("Ingrese el codigo del grupo: ")
    nombre = input("Ingrese el nombre del grupo: ")
    sigla = input("Ingrese la sigla del grupo: ")
    
    
    grupo = {
        "codigo" : codigo,
        "nombre" : nombre,
        "sigla" : sigla
    }


    try:
        with open("data/grupos.json", "r") as archivo:
            grupos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        grupos = []
        
    grupos.append(grupo)
    try:
        with open("data/grupos.json", "w") as archivo:
            json.dump(grupos, archivo)
            print("Grupo registrado correctamente.")
    except (FileNotFoundError, json.JSONDecodeError):
        # Crear la carpeta si no existe
        os.makedirs("data", exist_ok=True)
