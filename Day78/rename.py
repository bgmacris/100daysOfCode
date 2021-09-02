import os

PATH = input("Introduce la ruta del directorio que contiene los archivos: ")
NAME = input("Nombre con el que renombrar los archivos: ")
COUNT = 0

files = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]
for file in files:
    os.rename(os.path.join(PATH, file), os.path.join(PATH, os.path.join(PATH, f'{NAME}{COUNT}')))
    COUNT = COUNT + 1
