import hashlib
import json
import os
from . import menu # Importacion relativa
# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función de inicio de sesión
def iniciar_sesion():
    os.system('clear' if os.name != 'nt' else 'cls')
    print("=======================================")
    print("           INICIO DE SESIÓN           ")
    print("=======================================")   


    usuario = input("Ingrese su usuario: ")
    while True:
        contraseña_guardada = cargar_contraseña()
        contraseña = input("Ingrese la contraseña: ")

        if encriptar_contraseña(contraseña) == contraseña_guardada:
            print("\nAcceso concedido\n")
            break
        else:
            os.system("clear")
            print(">>> Error. Contraseña incorrecta")
            input("Presione enter para continuar. . .")
            os.system("clear")

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
        print(f">>> Error al guardar la contraseña: {e}")


# Limpiar la consola antes de iniciar sesión
os.system("clear")

# Iniciar sesión
iniciar_sesion()

# Mostrar el menú después de un inicio de sesión exitoso
os.system("clear")
menu.mostrar_menu  # Asegúrate de que la función menu() esté definida en 'interfaz'