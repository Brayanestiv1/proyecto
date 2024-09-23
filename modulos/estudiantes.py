import json
import os

def registrar_estudiante():
    print('\033c')
    # Solicitar datos del estudiante

    #Validacion de nombre
    
    while True:
        try:
            print('\033c')
            codigo = int(input("---> Ingrese el código del estudiante: "))
            if codigo <= 0:
                print("El código debe ser un número positivo.")
            else:
                break  # Si es un número positivo, salimos del bucle
        except ValueError:
            print('\033c')  # Limpia la consola
            print(">>> Error. Por favor, ingrese un número válido para el código.")
            input("Presione enter para volver a intentar. . . ")
            print('\033')

    while True:
        try:
            print('\033c')
            nombre = str(input("---> Ingrese el código del estudiante: "))
            if nombre == int:
                print("El nombre no puede contener numeros.")
            else:
                break  # Si el nombre esta bien, salimos del bucle
        except ValueError:
            print('\033c')  # Limpia la consola
            print(">>> Error. Por favor, ingrese un nombre válido.")
            input("Presione enter para volver a intentar. . . ")
            print('\033')

    while True:
        try:
            print('\033c')
            sexo = str(input("---> Ingrese el genero del estudiante (M/F): "))
            if nombre == "M" or nombre == "m" or nombre == "F" or nombre == "f":
                print("")
            else:
                break  # Si el genero esta bien, salimos del bucle
        except ValueError:
            print('\033c')  # Limpia la consola
            print(">>> Error. Por favor, ingrese un genero válido.")
            input("Presione enter para volver a intentar. . . ")
            print('\033')

    #Validacion de edad
    while True:
        try:
            edad = int(input("---> Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")


    # Crear el diccionario del estudiante
    estudiante = {
            "codigo": codigo,
            "nombre": nombre,
            "sexo": sexo,
            "edad": edad
        }

    # Intentar cargar los estudiantes existentes
    try:
        with open("data/estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        estudiantes = []

    # Agregar el nuevo estudiante a la lista
    estudiantes.append(estudiante)

    # Asegúrate de que la carpeta existe antes de guardar
    os.makedirs("proyecto/data", exist_ok=True)

    # Guardar la lista de estudiantes en el archivo
    try:
        with open("data/estudiantes.json", "w") as archivo:
            json.dump(estudiantes, archivo, indent=4)
        print("Estudiante registrado correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")
