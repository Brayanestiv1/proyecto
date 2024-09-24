import json
import os
def consultar_estudiantes_por_grupo():
    codigo_grupo = input("Ingrese el código del grupo: ")
    
    with open('data/asignaciones.json', 'r') as archivo:
        asignaciones = json.load(archivo)
    
    estudiantes = [asignacion['codigo_estudiante'] for asignacion in asignaciones if asignacion['codigo_grupo'] == codigo_grupo]
    
    print(f"Estudiantes en el grupo {codigo_grupo}:")
    for estudiante in estudiantes:
        print(estudiante)
