import json
import os

def mostrar_menu_registro_estudiantes():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("      📚 Registro de Estudiantes 📚      ")
    print("=" * 40)
    print("1. Ingresar Código del Estudiante")
    print("2. Ingresar Nombre del Estudiante")
    print("3. Ingresar Género del Estudiante (M/F)")
    print("4. Ingresar Edad del Estudiante")
    print("5. Guardar Estudiante")
    print("6. Volver al Menú Principal")
    print("=" * 40)

def registrar_estudiante():
    estudiantes = []

    # Intentar cargar estudiantes existentes
    try:
        with open("data/estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        estudiantes = []

    estudiante = {}
    
    while True:
        mostrar_menu_registro_estudiantes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                try:
                    codigo = int(input("---> Ingrese el código del estudiante: "))
                    if codigo <= 0:
                        print("El código debe ser un número positivo.")
                    else:
                        estudiante['codigo'] = codigo
                        break  # Si es un número positivo, salimos del bucle
                except ValueError:
                    print(">>> Error. Por favor, ingrese un número válido para el código.")
                    input("Presione enter para volver a intentar. . . ")
        
        elif opcion == "2":
            while True:
                nombre = input("---> Ingrese el nombre del estudiante: ").strip()
                if any(char.isdigit() for char in nombre):
                    print(">>> Error. El nombre no puede contener números.")
                elif not nombre:
                    print(">>> Error. El nombre no puede estar vacío.")
                else:
                    estudiante['nombre'] = nombre
                    break

        elif opcion == "3":
            while True:
                sexo = input("---> Ingrese el género del estudiante (M/F): ").strip().lower()
                if sexo in ["m", "f"]:
                    estudiante['sexo'] = sexo
                    break
                else:
                    print(">>> Error. Por favor, ingrese 'M' o 'F'.")

        elif opcion == "4":
            while True:
                try:
                    edad = int(input("---> Ingrese la edad del estudiante: "))
                    if edad <= 0:
                        print("La edad debe ser un número positivo.")
                    else:
                        estudiante['edad'] = edad
                        break
                except ValueError:
                    print(">>> Error. Por favor, ingrese un número válido para la edad.")

        elif opcion == "5":
            if all(key in estudiante for key in ['codigo', 'nombre', 'sexo', 'edad']):
                estudiantes.append(estudiante)
                # Asegúrate de que la carpeta existe antes de guardar
                os.makedirs("data", exist_ok=True)

                # Guardar la lista de estudiantes en el archivo
                try:
                    with open("data/estudiantes.json", "w") as archivo:
                        json.dump(estudiantes, archivo, indent=4)
                    print("\n✅ Estudiante registrado correctamente.")
                    input("Presione Enter para continuar...")
                except Exception as e:
                    print(f"⚠️ Error al guardar los datos: {e}")
            else:
                print(">>> ❌ Error. Debe completar todos los campos antes de guardar.")

        elif opcion == "6":
            print("👋 Volviendo al menú principal...")
            break

        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")

# Para probar la función (descomentar si se necesita)
# registrar_estudiante()
