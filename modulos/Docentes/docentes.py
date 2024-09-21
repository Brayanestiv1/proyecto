import json
import os

def lenCedula():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        cedula = input("Ingrese la cédula del docente (10 dígitos): ")
        
        if len(cedula) == 10 and cedula.isdigit():
            return int(cedula)  # Retorna la cédula válida
        else:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
            if not cedula.isdigit():
                print(">>> Error. Debe ingresar un número.")
                input("Presione cualquier tecla para volver a ingresar...")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
                print("La cédula debe tener exactamente 10 dígitos y contener solo números.")
                input("Presione cualquier tecla para volver a ingresar...")
            
docentes = {
    "nombre" : input("Ingrese un nombre: "),
    "cedula" : lenCedula()
    "materia" : lenMateria()
}

# Guardar en un archivo JSON
with open("modulos/Docentes/docentes.json", "w") as fd:
    json.dump(docentes, fd)


print("Dato guardado correctamente.")

