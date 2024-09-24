import hashlib
import json
import os
from . import menu  # Importación relativa
# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función de inicio de sesión
def iniciar_sesion():
    while True:  # Permitir múltiples intentos hasta que se logre el inicio de sesión
        os.system('clear' if os.name != 'nt' else 'cls')
        print("="*60)
        print("            📚 INICIO DE SESIÓN 📚            ")
        print("="*60)

        usuario = input("Ingrese su usuario: ").strip()

        # Validar que el nombre no contenga números
        if any(char.isdigit() for char in usuario):
            print(">>> ❌ Error. El nombre de usuario no puede contener números.")
            input("Presione enter para intentar de nuevo...")
            continue  # Volver a solicitar el nombre de usuario

        while True:
            contraseña_guardada = cargar_contraseña()
            contraseña = input("Ingrese la contraseña: ").strip()
            error_msg = ""

            if encriptar_contraseña(contraseña) == contraseña_guardada:
                print("\n  🎓 Acceso concedido. Bienvenido, {}! 🎓\n".format(usuario))
                input("Presione enter para ir al menu principal. . .")
                os.system("clear")  # Limpiar la consola después de ingresar
                return  # Salir de la función para mostrar el menú
            else:
                error_msg = ">>> ❌ Error. Contraseña incorrecta."
                print("\r" + " " * len(error_msg) + "\r", end="")  # Limpiar mensaje anterior
                print(error_msg)  # Imprimir mensaje de error
                input("Presione enter para intentar de nuevo...")

# Función para cargar la contraseña del archivo JSON
def cargar_contraseña():
    try:
        with open("data/contraseña.json", "r") as archivo:
            datos = json.load(archivo)
            return datos["contraseña"]
    except (FileNotFoundError, json.JSONDecodeError):
        # Crear la carpeta si no existe
        os.makedirs("data", exist_ok=True)
        # Guardar la contraseña predeterminada
        guardar_contraseña("SISGESA")
        # Cargar de nuevo la contraseña guardada
        return cargar_contraseña()

# Función para guardar la contraseña en el archivo JSON
def guardar_contraseña(contraseña):
    try:
        with open("data/contraseña.json", "w") as archivo:
            json.dump({"contraseña": encriptar_contraseña(contraseña)}, archivo)
    except Exception as e:
        print(f">>> ⚠️ Error al guardar la contraseña: {e}")

# Limpiar la consola antes de iniciar sesión
os.system("clear")

# Iniciar sesión
iniciar_sesion()

# Mostrar el menú después de un inicio de sesión exitoso
os.system("clear")
menu.mostrar_menu()  # Llama a la función mostrar_menu() de 'menu'
