# Importar módulos necesarios para el funcionamiento del programa
from interfaz import long, menu
from modulos import asig_estudiante_grup_modul, asistencia, consultas_generacion_informes, docentes, estudiantes, modulos, registro_asistencia, registro_grupos

def main():
    # Bucle principal del programa que se ejecuta indefinidamente hasta que se elija salir
    while True:
        # Mostrar el menú principal al usuario
        menu.mostrar_menu()
        # Solicitar al usuario que seleccione una opción
        opcion = input(">>> Seleccione una opción:? ")

        # Opciones del menú
        if opcion == "1":
            # Opción para registrar un grupo
            registro_grupos.registrar_grupo()
        elif opcion == "2":
            # Opción para registrar un módulo
            modulos.registrar_modulo()
        elif opcion == "3":
            # Opción para registrar un estudiante
            estudiantes.registrar_estudiante()
        elif opcion == "4":
            # Opción para registrar un docente
            docentes.registrar_docente()
        elif opcion == "5":
            # Opción para registrar asistencia (actualmente no implementada)
            pass
            # asistencia.registrar_asistencia()
        elif opcion == "6":
            # Opción para consultar estudiantes por grupo (actualmente no implementada)
            pass
            # consultas_generacion_informes.consultar_estudiantes_por_grupo()
        elif opcion == "7":
            # Opción para generar informes (actualmente no implementada)
            pass
            # consultas_generacion_informes()
        elif opcion == "8":
            # Opción para ejecutar una función adicional (actualmente no implementada)
            pass
            # long()
        elif opcion == "9":
            # Opción para salir del programa
            print("\n\nGracias por usar el software.\n")
            break  # Termina el bucle y cierra el programa
        else:
            # Mensaje de error si la opción no es válida
            print(">>> Error. Opción inválida. Intente de nuevo.")

# Ejecutar la función main si este archivo es el programa principal
if __name__ == "__main__":
    main()
