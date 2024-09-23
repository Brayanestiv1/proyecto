import json

def registrar_modulo():
    # Solicitar datos al usuario
    codigo = input("Ingrese el código del módulo: ")
    nombre = input("Ingrese el nombre del módulo: ")
    duracion = input("Ingrese la duración del módulo en semanas: ")

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
    with open('proyecto/data/modulos.json', 'w') as archivo:
        json.dump(modulos, archivo, indent=4)  # Formato JSON con indentación
    print("Módulo registrado correctamente.")


def listar_modulos():
    try:
        with open('data/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
            if not modulos:
                print("No hay módulos registrados.")
            else:
                for modulo in modulos:
                    print(f"Código: {modulo['codigo']}, Nombre: {modulo['nombre']}, Duración: {modulo['duracion']} semanas")
    except FileNotFoundError:
        print("No hay módulos registrados.")