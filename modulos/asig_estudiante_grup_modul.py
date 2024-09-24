import json
import os

def asignar_estudiantes():
    print('\033c')  # Limpia la consola
    print("="*30)
    print("     --- Asignar Estudiantes ---     ")
    print("="*30)

    codigo_estudiante = input("Ingrese el código del estudiante: ").strip()
    codigo_grupo = input("Ingrese el código del grupo: ").strip()

# Validación de códigos
    if not codigo_estudiante or not codigo_grupo:
        print(">>> Error. El código del estudiante y el grupo son obligatorios.")
        return

    modulos = []
    for i in range(1, 4):  # Permitir inscribir de 1 a 3 módulos
        codigo_modulo = input(f"Ingrese el código del módulo {i} (o presione Enter para finalizar): ")
        if codigo_modulo:
            modulos.append(codigo_modulo)
        else:
            break
    # Intentar cargar las asignaciones existentes
    try:
        with open("data/asignaciones.json", "r") as archivo:
            asignaciones = json.load(archivo)
    except FileNotFoundError:
        asignaciones = []
    except json.JSONDecodeError:
        print(">>> Error: El archivo de asignaciones está corrupto o no es un JSON válido.")
        return

    asignaciones.append({
        'codigo_estudiante': codigo_estudiante,
        'codigo_grupo': codigo_grupo,
        'modulos': modulos
    })

# Asegurarse de que la carpeta existe antes de guardar
    os.makedirs("data", exist_ok=True)

# Guardar la asignación
    try:
        with open('data/asignaciones.json', 'w') as archivo:
            json.dump(asignaciones, archivo, indent=4)  # Agregar indentación
        print("Estudiante asignado correctamente.")
    except Exception as e:
        print(f"Error al guardar la asignación: {e}")