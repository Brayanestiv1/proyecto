
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
        


def menu():
    while True:
        print('\033c')
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
            limpiar_pantalla()
            print("Opción no válida. Intente de nuevo.")
            input("Presiona cualquier tecla para continuar...")
        
# Inicio del programa
nombre = input("---> Usuario? ")
limpiar_pantalla()
valContr()
menu()
