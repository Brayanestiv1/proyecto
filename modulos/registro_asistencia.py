from datetime import datetime

def registrar_asistencia():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    codigo_modulo = input("Ingrese el código del módulo: ")
    
    entrada = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    salida = input("Ingrese la hora de salida (YYYY-MM-DD HH:MM:SS): ")  # Simulamos la entrada manual de salida
    
    asistencia = {
        'codigo_estudiante': codigo_estudiante,
        'codigo_modulo': codigo_modulo,
        'entrada': entrada,
        'salida': salida
    }

    try:
        with open('data/asistencia.json', 'r') as archivo:
            asistencias = json.load(archivo)
    except FileNotFoundError:
        asistencias = []

    asistencias.append(asistencia)

    with open('data/asistencia.json', 'w') as archivo:
        json.dump(asistencias, archivo)
    print("Asistencia registrada correctamente.")
