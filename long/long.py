import hashlib
import json
from menu import menu
# Función para encriptar la contraseña
def encriptar_contraseña(contraseña):
    return hashlib.sha256(contraseña.encode()).hexdigest()

# Función para cargar la contraseña del archivo JSON
def cargar_contraseña():
    try:
        with open('data/contraseña.json', 'r') as archivo:
            datos = json.load(archivo)
            return datos['contraseña']
    except FileNotFoundError:
        return encriptar_contraseña('SISGESA')  # Primera ejecución

# Función para guardar la contraseña en el archivo JSON
def guardar_contraseña(contraseña):
    with open('data/contraseña.json', 'w') as archivo:
        json.dump({'contraseña': encriptar_contraseña(contraseña)}, archivo)

# Función de inicio de sesión
def iniciar_sesion():
    contraseña_guardada = cargar_contraseña()
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if encriptar_contraseña(contraseña) == contraseña_guardada:
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")

