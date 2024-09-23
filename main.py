
while True:
    
    while True:
        op = menu()
        match op:
            case 1:
                registroDeGrupos()
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

