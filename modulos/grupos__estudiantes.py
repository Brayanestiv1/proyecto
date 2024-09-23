import json
import os
import subprocess
import platform

def limpiar_pantalla():
    if platform.system() == "Windows":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

gruEstudiantes = {}

