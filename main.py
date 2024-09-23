from long import long
from menu import menu
from modulos import asig_estudiante_grup_modul,asistencia,consultas_generacion_informes,docentes,estudiantes,modulos,registro_asistencia,registro_grupos
while True:
    long
    menu
    while True:
        op = menu()
        match op:
            case 1:
                registro_grupos
            case 2:
                registroDeModulos()
            case 3:
                registroDeEstudiantes()
            case 4:
                registroDeDocentes()
            case 5:
                registroDeAsistencia()
            case 6:
                consultasDeInformacion()
            case 7:
                ceneracionDeInformes()
            case 8:
                cambioDeContraseña()
            case 9:
                print("\n\nGracias por usar el sotware.\n")
                break
    break

print('\033c')

