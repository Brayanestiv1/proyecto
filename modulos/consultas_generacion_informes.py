import json
import os

def mostrar_menu_consulta_estudiantes():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("      📚 Consulta de Estudiantes por Grupo 📚      ")
    print("=" * 40)
    print("1. Consultar Estudiantes")
    print("2. Volver al Menú Principal")
    print("=" * 40)

def consultar_estudiantes_por_grupo():
    while True:
        mostrar_menu_consulta_estudiantes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_grupo = input("Ingrese el código del grupo: ").strip()
            
            try:
                with open('data/asignaciones.json', 'r') as archivo:
                    asignaciones = json.load(archivo)

                # Filtrar estudiantes por grupo
                estudiantes = [asignacion['codigo_estudiante'] for asignacion in asignaciones if asignacion['codigo_grupo'] == codigo_grupo]
                
                if estudiantes:
                    print(f"Estudiantes en el grupo {codigo_grupo}:")
                    for estudiante in estudiantes:
                        print(f"- {estudiante}")
                else:
                    print(f"No hay estudiantes registrados en el grupo {codigo_grupo}.")

                input("Presione Enter para continuar...")

            except FileNotFoundError:
                print("No se encontraron asignaciones. Asegúrese de que el archivo exista.")
                input("Presione Enter para continuar...")

        elif opcion == "2":
            print("👋 Volviendo al menú principal...")
            break

        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")
