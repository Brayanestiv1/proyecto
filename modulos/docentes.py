import json
import os

def mostrar_menu_registro_docentes():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("        📚 Registro de Docentes 📚        ")
    print("=" * 40)
    print("1. Ingresar Cédula del Docente")
    print("2. Ingresar Nombre del Docente")
    print("3. Asignar Módulos al Docente")
    print("4. Asignar Grupo al Docente")
    print("5. Guardar Docente")
    print("6. Volver al Menú Principal")
    print("7. Listar Docentes")
    print("=" * 40)

def registrar_docente():
    docentes = []

    # Intentar cargar docentes existentes
    try:
        with open("data/docentes.json", "r") as archivo:
            docentes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        docentes = []

    while True:
        mostrar_menu_registro_docentes()
        docente = {
            'modulos': [],  # Inicializar la lista de módulos
            'grupo': None   # Inicializar el grupo
        }

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = input("---> Ingrese la cédula del docente: ").strip()
            docente['cedula'] = cedula

        elif opcion == "2":
            nombre = input("---> Ingrese el nombre del docente: ").strip()
            if nombre:
                docente['nombre'] = nombre
            else:
                print(">>> ❌ Error. El nombre no puede estar vacío.")

        elif opcion == "3":
            # Asignar hasta 3 módulos al docente
            for i in range(1, 4):
                modulo = input(f"---> Ingrese el código del módulo {i} (o presione Enter para finalizar): ").strip()
                if modulo:
                    docente['modulos'].append(modulo)
                else:
                    break  # Salir del bucle si no se ingresa un módulo

        elif opcion == "4":
            grupo = input("---> Ingrese el código del grupo al que se asignará al docente: ").strip()
            if grupo:
                docente['grupo'] = grupo
            else:
                print(">>> ❌ Error. Debe ingresar un código de grupo.")

        elif opcion == "5":
            if all(key in docente for key in ['cedula', 'nombre']):
                docentes.append(docente)
                # Asegúrate de que la carpeta existe antes de guardar
                os.makedirs("data", exist_ok=True)

                # Guardar la lista de docentes en el archivo
                try:
                    with open("data/docentes.json", "w") as archivo:
                        json.dump(docentes, archivo, indent=4)
                    print("\n✅ Docente registrado correctamente.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f"⚠️ Error al guardar los datos: {e}")
            else:
                print(">>> ❌ Error. Debe completar todos los campos antes de guardar.")

        elif opcion == "6":
            print("👋 Volviendo al menú principal...")
            break

        elif opcion == "7":
            listar_docentes()  # Llamar a listar_docentes sin pasar la lista

        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")

def listar_docentes():
    try:
        # Intentar cargar docentes existentes
        with open("data/docentes.json", "r") as archivo:
            docentes = json.load(archivo)

            if not docentes:
                print("No hay docentes registrados.")
                return

            print("=" * 40)
            print("        📚 Lista de Docentes 📚        ")
            print("=" * 40)

            for docente in docentes:
                print(f"Cédula: {docente['cedula']}, Nombre: {docente['nombre']}")
                if docente['modulos']:
                    print("  Módulos Asignados:", ", ".join(docente['modulos']))
                else:
                    print("  Módulos Asignados: Ninguno")
                
                if docente['grupo']:
                    print(f"  Grupo Asignado: {docente['grupo']}")
                else:
                    print("  Grupo Asignado: Ninguno")
    
            input("Presione Enter para continuar...")  # Para que el usuario pueda ver la lista

    except FileNotFoundError:
        print("No hay docentes registrados.")
    except json.JSONDecodeError:
        print("Error al leer los datos de los docentes.")

# Para probar la función (descomentar si se necesita)
# registrar_docente()

