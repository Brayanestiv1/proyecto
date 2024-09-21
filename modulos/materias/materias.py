import json
import os

materias= {}

matPrimaria = {
    1:"latemáticas",
    2:"lengua y literatura",
    3:"ciencias naturales",
    4:"ciencias sociales",
    5:"educacion fisica",
    6:"arte",
    7:"ingles",
}


matSecundaria = {
    1:"matemáticas",
    2:"lengua y literatura",
    3:"ciencias naturales",
    4:"ciencias sociales",
    5:"educacion fisica",
    6:"arte",
    7:"ingles",
    8:"tecnologia o informatica",
    9:"educacion civica y etica",
}

matBachillerato = {
    1:"matemáticas",
    2:"literatura",
    3:"biología",
    4:"química",
    5:"física",
    6:"historia",
    7:"geografía",
    8:"economía",
    9:"inglés",
    10:"educación Física",
    11:"arte",
    12:"filosofía",
}

materias = {
    "primaria":matPrimaria,
    "secundaria":matSecundaria,
    "bachillerato":matBachillerato
}
# Guardar en un archivo JSON
with open("modulos/materias/materias.json", "w", encoding="utf-8") as fd:
    json.dump(materias, fd, ensure_ascii=False)


print("Dato guardado correctamente.")