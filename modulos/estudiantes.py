def registrar_estudiante():
    # Solicitar datos del estudiante
    codigo = input("Ingrese el código del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    sexo = input("Ingrese el sexo del estudiante (M/F): ")
    edad = input("Ingrese la edad del estudiante: ")
    
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
        'codigo': codigo,
        'nombre': nombre,
        'sexo': sexo,
        'edad': edad
    }

    # Intentar cargar los estudiantes existentes
    try:
        with open('proyecto/data/estudiantes.json', 'r') as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        estudiantes = []

    # Agregar el nuevo estudiante a la lista
    estudiantes.append(estudiante)

    # Guardar la lista de estudiantes en el archivo
    with open('proyecto/data/estudiantes.json', 'w') as archivo:
        json.dump(estudiantes, archivo, indent=4)
    print("Estudiante registrado correctamente.")
