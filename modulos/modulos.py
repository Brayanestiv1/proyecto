import json
import os

def mostrar_menu_registro_modulos():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("        📚 Registro de Módulos 📚        ")
    print("=" * 40)
    print("1. Ingresar Código del Módulo")
    print("2. Ingresar Nombre del Módulo")
    print("3. Ingresar Duración del Módulo")
    print("4. Guardar Módulo")
    print("5. Listar Módulos")
    print("6. Volver al Menú Principal")
    print("=" * 40)

def registrar_modulo():
    modulos = []

    # Intentar cargar módulos existentes
    try:
        with open('data/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        modulos = []

    modulo = {}
    mostrar_menu_registro_modulos()

    while True:
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            modulo["codigo"] = (input("Ingrese el código del módulo: "))
        elif opcion == "2":
            nombre = input("Ingrese el nombre del módulo: ").strip()
            if nombre:
                modulo['nombre'] = nombre
            else:
                print(">>> ❌ Error. El nombre no puede estar vacío.")
        elif opcion == "3":
            duracion = int(input("Ingrese la duración del módulo en semanas: "))
            modulo['duracion'] = duracion
        elif opcion == "4":
            if all(key in modulo for key in ['codigo', 'nombre', 'duracion']):
                modulos.append(modulo)
                # Guardar módulos en el archivo
                try:
                    os.makedirs("data", exist_ok=True)
                    with open("data/modulos.json", "w") as archivo:
                        json.dump(modulos, archivo, indent=4)  # Formato JSON con indentación
                    print("✅ Módulo registrado correctamente.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f">>> ⚠️ Error al guardar el módulo: {e}")
            else:
                print(">>> ❌ Error. Debe completar todos los campos antes de guardar.")
        elif opcion == "5":
            listar_modulos(modulos)
        elif opcion == "6":
            print("👋 Volviendo al menú principal...")
            break
        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")

        mostrar_menu_registro_modulos()

def listar_modulos(modulos):
    if not modulos:
        print("No hay módulos registrados.")
    else:
        for modulo in modulos:
            print(f"Código: {modulo['codigo']}, Nombre: {modulo['nombre']}, Duración: {modulo['duracion']} semanas")
    input("Presione Enter para continuar...")

# Para probar la función (descomentar si se necesita)
# registrar_modulo()
