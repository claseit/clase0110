import sys
import os

argumentos = sys.argv

try:
    ruta = argumentos[1]
    ext = argumentos[2]
except IndexError:
    print("Faltan Argumentos")
    sys.exit()

if not ext.startswith("."):
    ext = "." + ext

try:
    archivos = os.listdir(ruta)
except FileNotFoundError:
    print("No existe el directorio")
    sys.exit()

print("-------------------------------------------------")

print("Los archivos en",ruta,"terminados con",ext,"son: ")

for n in archivos:
    if n.endswith(ext):
        print(n)

print("-------------------------------------------------")
