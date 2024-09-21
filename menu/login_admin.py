import subprocess
import platform

"""1. Inicio de Sesión: 
Al iniciar el programa, debe solicitarse un nombre de usuario y contraseña. 
La primera vez que el sistema sea ejecutado, la contraseña será la predefinida: "SISGESA"""
def limpiar_pantalla():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)


contr = "SISGESA"

def valContr():
    while True:
       
        contraseña = (input("---> Contraseña? "))
        if contraseña == contr:
            
            print("** Contraseña Correcta **")
            break
        else:
            limpiar_pantalla()
            print(">>> Error. Contraseña incorrecta")
            input("Presiona cualquier tecla para volver a intentarlo. . .") 
            limpiar_pantalla()
        

"""2. Menú de Opciones:
El programa debe presentar un menú con opciones claras para interactuar con 
el sistema."""
def menu():
    while True:
        limpiar_pantalla()
        print("        ** MENU **")
        print(" 1. Registro de grupos.")
        print(" 2. Registro de módulos.")
        print(" 3. Registro de estudiantes")
        print(" 4. Registro de docentes.") 
        print(" 5. Registro de asistencia.")
        print(" 6. Consultas de información.")
        print(" 7. Generación de informes.")
        print(" 8. Cambio de contraseña.")
        print(" 9. Salida del sistema.")

        opcion = input(">>> Opcion? ")
        
        if opcion == '9':
            print("Saliendo del sistema...")
            break
        elif opcion in '12345678':
            print(f"Has seleccionado la opción {opcion}.")
            input("Presiona cualquier tecla para continuar...")
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presiona cualquier tecla para continuar...")
        
# Inicio del programa
nombre = input("---> Usuario? ")
limpiar_pantalla()
valContr()
menu()
