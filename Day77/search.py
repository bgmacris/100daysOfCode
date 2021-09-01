import os

global PATH, FILE, FOUND_FILE
PATH = input("Introduce la ruta del directorio que quieres explorar: ")
# FILE = input("Introduce el nombre del archivo que quieres encontrar:")
FILE = 'search.py'
FOUND_FILE = []

def get_subfolders(PATH):
    subfolders = [f.path for f in os.scandir(PATH) if f.is_dir()]
    return subfolders

subfolders = get_subfolders(PATH)
cont = 0

if subfolders:
    def search_in_folder(subfolders):
        global FOUND_FILE
        for folder in subfolders:
            if folder == 'C:\\Users\\Bogdan\\Documents\\GitHub\\100daysOfCode\\Day1':
                print(get_subfolders(folder))
            files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            for f in files:
                name_file = FILE
                if '.' in FILE:
                    name_file = FILE.split('.')
                if name_file in f.split('.') or name_file == f.split('.'):
                    SEARCH = False
                    FOUND_FILE.append(os.path.join(folder, f))
            subfolders = subfolders + get_subfolders(folder)
            subfolders.remove(folder)
        if subfolders:
            search_in_folder(subfolders)
        else:
            return FOUND_FILE
    
    search_in_folder(subfolders)

if FOUND_FILE:
    print("ESTOS SON LOS ARCHIVOS QUE SE HAN ENCONTRADO")   
    for i in FOUND_FILE:
        print(i)
else:
    print("NO SE HA ENCONTRADO NINGUN ARCHIVO")
