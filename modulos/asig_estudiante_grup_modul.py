def asignar_estudiantes():
    codigo_estudiante = input("Ingrese el código del estudiante: ")
    codigo_grupo = input("Ingrese el código del grupo: ")
    modulos = []
    for i in range(1, 4):  # Permitir inscribir de 1 a 3 módulos
        codigo_modulo = input(f"Ingrese el código del módulo {i} (o presione Enter para finalizar): ")
        if codigo_modulo:
            modulos.append(codigo_modulo)
        else:
            break
    
    # Guardar la asignación
    try:
        with open('data/asignaciones.json', 'r') as archivo:
            asignaciones = json.load(archivo)
    except FileNotFoundError:
        asignaciones = []

    asignaciones.append({
        'codigo_estudiante': codigo_estudiante,
        'codigo_grupo': codigo_grupo,
        'modulos': modulos
    })

    with open('data/asignaciones.json', 'w') as archivo:
        json.dump(asignaciones, archivo)
    print("Estudiante asignado correctamente.")
