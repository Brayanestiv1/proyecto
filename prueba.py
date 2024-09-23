import json

# Función para registrar módulos
def registrar_modulo():
    codigo = input("Ingrese el código del módulo: ")
    nombre = input("Ingrese el nombre del módulo: ")
    duracion = input("Ingrese la duración del módulo en semanas: ")

    modulo = {
        'codigo': codigo,
        'nombre': nombre,
        'duracion': duracion
    }

    try:
        with open('data/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
    except FileNotFoundError:
        modulos = []

    modulos.append(modulo)

    with open('data/modulos.json', 'w') as archivo:
        json.dump(modulos, archivo, indent=4)
    print("Módulo registrado correctamente.")

# Función para registrar estudiantes
def registrar_estudiante():
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    sexo = input("Ingrese el sexo del estudiante (M/F): ")

    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la edad.")

    estudiante = {
        'codigo': codigo,
        'nombre': nombre,
        'sexo': sexo,
        'edad': edad
    }

    try:
        with open('data/estudiantes.json', 'r') as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        estudiantes = []

    estudiantes.append(estudiante)

    # Guardar la lista de estudiantes en el archivo
    
    with open('data/estudiantes.json', 'w') as archivo:
        json.dump(estudiantes, archivo, indent=4)
    print("Estudiante registrado correctamente.")

# Función para registrar docentes
def registrar_docente():
    cedula = input("Ingrese la cédula del docente: ")
    nombre = input("Ingrese el nombre del docente: ")

    docente = {
        'cedula': cedula,
        'nombre': nombre
    }

    try:
        with open('data/docentes.json', 'r') as archivo:
            docentes = json.load(archivo)
    except FileNotFoundError:
        docentes = []

    docentes.append(docente)

    with open('data/docentes.json', 'w') as archivo:
        json.dump(docentes, archivo, indent=4)
    print("Docente registrado correctamente.")

# Función para listar estudiantes
def consultar_estudiantes():
    try:
        with open('data/estudiantes.json', 'r') as archivo:
            estudiantes = json.load(archivo)
            if not estudiantes:
                print("No hay estudiantes registrados.")
            else:
                for estudiante in estudiantes:
                    print(f"Código: {estudiante['codigo']}, Nombre: {estudiante['nombre']}, Sexo: {estudiante['sexo']}, Edad: {estudiante['edad']}")
    except FileNotFoundError:
        print("No hay estudiantes registrados.")

# Función para listar módulos
def consultar_modulos():
    try:
        with open('data/modulos.json', 'r') as archivo:
            modulos = json.load(archivo)
            if not modulos:
                print("No hay módulos registrados.")
            else:
                for modulo in modulos:
                    print(f"Código: {modulo['codigo']}, Nombre: {modulo['nombre']}, Duración: {modulo['duracion']} semanas")
    except FileNotFoundError:
        print("No hay módulos registrados.")

# Función para listar docentes
def consultar_docentes():
    try:
        with open('data/docentes.json', 'r') as archivo:
            docentes = json.load(archivo)
            if not docentes:
                print("No hay docentes registrados.")
            else:
                for docente in docentes:
                    print(f"Cédula: {docente['cedula']}, Nombre: {docente['nombre']}")
    except FileNotFoundError:
        print("No hay docentes registrados.")

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n---- Menú Principal ----")
    print("1. Registrar Módulo")
    print("2. Registrar Estudiante")
    print("3. Registrar Docente")
    print("4. Consultar Estudiantes Registrados")
    print("5. Consultar Módulos Registrados")
    print("6. Consultar Docentes Registrados")
    print("7. Salir")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_modulo()
        elif opcion == "2":
            registrar_estudiante()
        elif opcion == "3":
            registrar_docente()
        elif opcion == "4":
            consultar_estudiantes()
        elif opcion == "5":
            consultar_modulos()
        elif opcion == "6":
            consultar_docentes()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
