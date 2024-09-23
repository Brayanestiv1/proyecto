def registrar_docente():
    # Solicitar datos del docente
    cedula = input("Ingrese la cédula del docente: ")
    nombre = input("Ingrese el nombre del docente: ")

    # Crear el diccionario del docente
    docente = {
        'cedula': cedula,
        'nombre': nombre
    }

    # Intentar cargar los docentes existentes
    try:
        with open('data/docentes.json', 'r') as archivo:
            docentes = json.load(archivo)
    except FileNotFoundError:
        docentes = []

    # Agregar el nuevo docente a la lista
    docentes.append(docente)

    # Guardar la lista de docentes en el archivo
    with open('data/docentes.json', 'w') as archivo:
        json.dump(docentes, archivo, indent=4)
    print("Docente registrado correctamente.")

