import json

def lenCedula():
    while True:
        cedula = int(input("Ingrese la celuda del docente: "))
        if len(str(cedula)) <= 10:
            return int(cedula)
docentes = {
    "nombre" : input("Ingrese un nombre: "),
    "cedula" : lenCedula()
}

# Guardar en un archivo JSON
with open("modulos/Docentes/docentes.json", "w") as fd:
    json.dump(docentes, fd)


print("Dato guardado correctamente.")

