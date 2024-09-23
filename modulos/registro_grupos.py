def registro_grupo():
    codigo = input("Ingrese el codigo del grupo: ")
    nombre = input("Ingrese el nombre del grupo: ")
    sigla = input("Ingrese la sigla del grupo: ")
    
    
    grupo = {
        "codigo" : codigo,
        "nombre" : nombre,
        "sigla" : sigla
    }


    try:
        with open("proyecto/data/grupos.json", "r") as archivo:
            grupos = json.load(archivo)
    except FileExistsError:
        grupos = []
        
    grupos.append(grupo)
    
    with open('data/grupos.json', 'w') as archivo:
        json.dump(grupos, archivo)
    print("Grupo registrado correctamente.")