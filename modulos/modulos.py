import json
import os
def registrar_modulo():
    # Solicitar datos al usuario
    codigo = int(input("Ingrese el código del módulo: "))
    nombre = str(input("Ingrese el nombre del módulo: "))
    duracion = int(input("Ingrese la duración del módulo en semanas: "))

    # Crear el diccionario del módulo
    modulo = {
        'codigo': codigo,
        'nombre': nombre,
        'duracion': duracion
    }

    # Intentar cargar los módulos existentes
    try:
        with open('proyecto/data/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
    except FileNotFoundError:
        modulos = []

    # Agregar el nuevo módulo a la lista
    modulos.append(modulo)

    # Guardar la lista de módulos actualizada en el archivo
    try:
        with open("data/modulos.json", "w") as archivo:
            json.dump(modulos, archivo, indent=4)  # Formato JSON con indentación
        print("Módulo registrado correctamente.")
    except (FileNotFoundError, json.JSONDecodeError):
        # Crear la carpeta si no existe
        os.makedirs("data", exist_ok=True)


def listar_modulos():
    try:
        with open("data/modulos.json", "r") as archivo:
            modulos = json.load(archivo)
            if not modulos:
                print("No hay módulos registrados.")
            else:
                for modulo in modulos:
                    print(f"Código: {modulo['codigo']}, Nombre: {modulo['nombre']}, Duración: {modulo['duracion']} semanas")
    except FileNotFoundError:
        print("No hay módulos registrados.")