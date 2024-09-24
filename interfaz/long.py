import hashlib  # Para encriptar contraseñas
import json  # Para manejar archivos JSON
import os  # Para operaciones del sistema, como limpiar la consola
from . import menu  # Importación relativa del módulo 'menu'

# Función para encriptar la contraseña usando SHA-256
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función de inicio de sesión
def iniciar_sesion():
    while True:  # Permitir múltiples intentos hasta que se logre el inicio de sesión
        os.system('clear' if os.name != 'nt' else 'cls')  # Limpiar la consola
        print("="*60)
        print("            📚 INICIO DE SESIÓN 📚            ")
        print("="*60)

        usuario = input("---> Ingrese su usuario: ").strip()  # Solicitar nombre de usuario

        # Validar que el nombre no contenga números
        if any(char.isdigit() for char in usuario):
            print(">>> ❌ Error. El nombre de usuario no puede contener números.")
            input("Presione enter para intentar de nuevo...")
            continue  # Volver a solicitar el nombre de usuario

        while True:  # Bucle para ingresar la contraseña
            contraseña_guardada = cargar_contraseña()  # Cargar la contraseña guardada
            contraseña = input("---> Ingrese la contraseña: ").strip()  # Solicitar contraseña
            error_msg = ""

            # Comparar la contraseña ingresada con la guardada
            if encriptar_contraseña(contraseña) == contraseña_guardada:
                print("\n  🎓 Acceso concedido. Bienvenido, {}! 🎓\n".format(usuario))
                input("Presione enter para ir al menu principal. . .")  # Esperar entrada del usuario
                os.system("clear")  # Limpiar la consola después de ingresar
                return  # Salir de la función para mostrar el menú
            else:
                print(">>> ❌ Error. Contraseña incorrecta.")  # Mensaje de error si la contraseña es incorrecta
                input("Presione enter para intentar de nuevo...")  # Esperar entrada del usuario

# Función para cargar la contraseña del archivo JSON
def cargar_contraseña():
    try:
        with open("data/contraseña.json", "r") as archivo:  # Intentar abrir el archivo de contraseña
            datos = json.load(archivo)  # Cargar datos JSON
            return datos["contraseña"]  # Retornar la contraseña guardada
    except (FileNotFoundError, json.JSONDecodeError):
        # Crear la carpeta 'data' si no existe
        os.makedirs("data", exist_ok=True)
        # Guardar la contraseña predeterminada
        guardar_contraseña("SISGESA")  # Llamar a la función para guardar la contraseña predeterminada
        # Cargar de nuevo la contraseña guardada
        return cargar_contraseña()

# Función para guardar la contraseña en el archivo JSON
def guardar_contraseña(contraseña):
    try:
        with open("data/contraseña.json", "w") as archivo:  # Abrir el archivo para escritura
            json.dump({"contraseña": encriptar_contraseña(contraseña)}, archivo)  # Guardar la contraseña encriptada
    except Exception as e:
        print(f">>> ⚠️ Error al guardar la contraseña: {e}")  # Mensaje de error si hay un problema al guardar

# Limpiar la consola antes de iniciar sesión
os.system("clear")

# Iniciar sesión
iniciar_sesion()

# Mostrar el menú después de un inicio de sesión exitoso
os.system("clear")
menu.mostrar_menu()  # Llama a la función mostrar_menu() de 'menu'
