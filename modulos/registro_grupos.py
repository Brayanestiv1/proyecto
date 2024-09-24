import os
import json

def mostrar_menu_registro():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("        📚 Registro de Grupos 📚        ")
    print("=" * 40)
    print("1. Ingresar Código del Grupo")
    print("2. Ingresar Nombre del Grupo")
    print("3. Ingresar Sigla del Grupo")
    print("4. Guardar Grupo")
    print("5. Asignar Estudiante a un Grupo y Módulos")
    print("6. Volver al Menú Principal")
    print("=" * 40)

def obtener_codigo_unico(grupos):
    codigo = input("Ingrese el código del grupo: ").strip()
    if any(grupo['codigo'] == codigo for grupo in grupos):
        print(">>> ❌ Error. El código ya existe. Intente de nuevo.")
        return obtener_codigo_unico(grupos)
    return codigo

def registrar_grupo():
    grupos = []

    # Intentar cargar grupos existentes desde el archivo JSON
    try:
        with open("data/grupos.json", "r") as archivo:
            grupos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        grupos = []

    grupo = {}
    mostrar_menu_registro()

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            grupo['codigo'] = obtener_codigo_unico(grupos)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del grupo: ").strip()
            if nombre:
                grupo['nombre'] = nombre
            else:
                print(">>> ❌ Error. El nombre no puede estar vacío.")
        elif opcion == "3":
            sigla = input("Ingrese la sigla del grupo: ").strip()
            if sigla:
                grupo['sigla'] = sigla
            else:
                print(">>> ❌ Error. La sigla no puede estar vacía.")
        elif opcion == "4":
            if all(key in grupo for key in ['codigo', 'nombre', 'sigla']):
                grupos.append(grupo)
                # Guardar grupos en el archivo
                try:
                    os.makedirs("data", exist_ok=True)
                    with open("data/grupos.json", "w") as archivo:
                        json.dump(grupos, archivo, indent=4)
                    print("✅ Grupo registrado correctamente.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f">>> ⚠️ Error al guardar el grupo: {e}")
                continue
            else:
                print(">>> ❌ Error. Debe completar todos los campos antes de guardar.")
        elif opcion == "5":
            asignar_estudiante_a_grupo_y_modulos(grupos)
        elif opcion == "6":
            print("👋 Volviendo al menú principal...")
            break
        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")

        mostrar_menu_registro()

def asignar_estudiante_a_grupo_y_modulos(grupos):
    # Cargar estudiantes existentes
    try:
        with open("data/estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = []

    # Verificar si hay grupos disponibles
    if not grupos:
        print(">>> ❌ No hay grupos registrados.")
        input("Presione Enter para continuar...")
        return

    # Mostrar grupos disponibles
    print("Grupos disponibles:")
    for grupo in grupos:
        print(f"Código: {grupo['codigo']}, Nombre: {grupo['nombre']}")

    # Seleccionar grupo
    codigo_grupo = input("Ingrese el código del grupo al que desea agregar un estudiante: ").strip()
    grupo_seleccionado = next((g for g in grupos if g['codigo'] == codigo_grupo), None)

    if grupo_seleccionado is None:
        print(">>> ❌ El código del grupo no es válido.")
        input("Presione Enter para continuar...")
        return

    # Mostrar estudiantes disponibles
    if not estudiantes:
        print(">>> ❌ No hay estudiantes registrados.")
        input("Presione Enter para continuar...")
        return

    print("Estudiantes disponibles:")
    for estudiante in estudiantes:
        print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}")

    # Seleccionar estudiante
    codigo_estudiante = input("Ingrese el código del estudiante a agregar: ").strip()
    estudiante_seleccionado = next((e for e in estudiantes if e['codigo'] == codigo_estudiante), None)

    if estudiante_seleccionado is None:
        print(">>> ❌ El código del estudiante no es válido.")
        input("Presione Enter para continuar...")
        return

    # Asignar el estudiante al grupo
    if 'estudiantes' not in grupo_seleccionado:
        grupo_seleccionado['estudiantes'] = []  # Inicializa la lista si no existe
    grupo_seleccionado['estudiantes'].append(estudiante_seleccionado)

    # Asignar módulos al estudiante
    modulos = []
    while len(modulos) < 3:
        modulo = input(f"Ingrese el código del módulo {len(modulos) + 1} (o presione Enter para finalizar): ").strip()
        if modulo:
            modulos.append(modulo)
        else:
            break  # Salir del bucle si no se ingresa un módulo

    # Guardar módulos en el estudiante
    estudiante_seleccionado['modulos'] = modulos

    # Guardar grupos actualizados
    try:
        with open("data/grupos.json", "w") as archivo:
            json.dump(grupos, archivo, indent=4)
        print("✅ Estudiante agregado al grupo y módulos correctamente.")
        input("Presione Enter para continuar...")
    except Exception as e:
        print(f">>> ⚠️ Error al guardar el grupo: {e}")

# Para probar la función (descomentar si se necesita)
# registrar_grupo()
