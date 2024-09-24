import json
import os
from datetime import datetime

def mostrar_menu_asistencia():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=" * 40)
    print("        📚 Registro de Asistencia 📚        ")
    print("=" * 40)
    print("1. Registrar Asistencia")
    print("2. Volver al Menú Principal")
    print("=" * 40)

def registrar_asistencia():
    asistencias = []

    # Intentar cargar asistencias existentes
    try:
        with open("data/asistencias.json", "r") as archivo:
            asistencias = json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        asistencias = []

    while True:
        mostrar_menu_asistencia()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo_estudiante = input("---> Ingrese el código del estudiante: ").strip()
            codigo_modulo = input("---> Ingrese el código del módulo: ").strip()
            fecha_hora_entrada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Simulación de salida: En un caso real, esto debería ser un evento posterior.
            fecha_hora_salida = input("---> Ingrese la fecha y hora de salida (dejar vacío para usar ahora): ").strip()
            if not fecha_hora_salida:
                fecha_hora_salida = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Crear el registro de asistencia
            asistencia = {
                'codigo_estudiante': codigo_estudiante,
                'codigo_modulo': codigo_modulo,
                'fecha_hora_entrada': fecha_hora_entrada,
                'fecha_hora_salida': fecha_hora_salida
            }
            asistencias.append(asistencia)

            # Guardar asistencias en el archivo
            try:
                os.makedirs("data", exist_ok=True)
                with open("data/asistencias.json", "w") as archivo:
                    json.dump(asistencias, archivo, indent=4)
                print("✅ Asistencia registrada correctamente.")
            except Exception as e:
                print(f"⚠️ Error al guardar la asistencia: {e}")

            input("Presione Enter para continuar...")

        elif opcion == "2":
            print("👋 Volviendo al menú principal...")
            break

        else:
            print(">>> ❌ Opción no válida. Intente de nuevo.")

# Para probar la función (descomentar si se necesita)
# registrar_asistencia()
