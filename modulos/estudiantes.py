import json
import os

def registrar_estudiante():
    print('\033c')
    # Solicitar datos del estudiante

    #Validacion de nombre
    
    while True:
        try:
            codigo = int(input("Ingrese el código del estudiante: "))
            if codigo <= 0:
                print("El codigo debe ser un número positivo.")
                continue
            break
        except ValueError:
            print('\033c')
            print(">>> Error. Por favor, ingrese un número válido para el codigo.")
        
    nombre = input("Ingrese el nombre del estudiante: ")
    if codigo != str:
        print(">>> Error. El dato ingresado es invalido.")
        input("Presione enter para volver a ingresar el dato requerido.")

    sexo = input("Ingrese el sexo del estudiante (M/F): ")
    if codigo != str:
        print(">>> Error. El dato ingresado es invalido.")
        input("Presione enter para volver a ingresar el dato requerido.")

    #Validacion de edad
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
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
