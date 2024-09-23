
def menu():
    while True:
        print('\033c')
        print("\n--- Menú Principal ---")
        print("1. Registro de grupos")
        print("2. Registro de módulos")
        print("3. Registro de estudiantes")
        print("4. Registro de docentes")
        print("5. Asignar estudiantes a grupos y módulos")
        print("6. Registrar asistencia")
        print("7. Consultas")
        print("8. Generación de informes")
        print("9. Cambio de contraseña")
        print("10. Salir")

        opcion = input(">>> Seleccione una opción:? ")
        
        if opcion == '10':
            print("Saliendo del sistema...")
            break
        elif opcion in '12345678910':
            print(f"Has seleccionado la opción {opcion}.")
            input("Presiona cualquier tecla para continuar...")
        else:
            print('\033c')
            print("Opción no válida. Intente de nuevo.")
            input("Presiona cualquier tecla para continuar...")
        
# Inicio del programa
nombre = input("---> Usuario? ")
limpiar_pantalla()
valContr()
menu()


