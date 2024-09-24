from interfaz import long,menu
from modulos import asig_estudiante_grup_modul,asistencia,consultas_generacion_informes,docentes, estudiantes,modulos, registro_asistencia, registro_grupos

def main():
    while True:
        menu.mostrar_menu()
        opcion = input(">>> Seleccione una opción:? ")
            
        if opcion == "1":
            registro_grupos.registrar_grupo()
        elif opcion == "2":
            modulos.registrar_modulo()
        elif opcion == "3":
            estudiantes.registrar_estudiante()
        elif opcion == "4":
            docentes.registrar_docente()
        elif opcion == "5":
            asistencia.registrar_asistencia()
        elif opcion == "6":
            consultas_generacion_informes.consultar_estudiantes_por_grupo()
        elif opcion == "7":
            consultas_generacion_informes()
        elif opcion == "8":
            long()
        elif opcion == "9":
            print("\n\nGracias por usar el sotware.\n")
            break
        else:
            print(">>> Error. Opcion invalida. Intente de nuevo.")

if __name__ == "__main__":
    main()

