import os
import shutil


global PATH
PATH = input("Ruta del directorio que quieres ordenar: ")

ext_text = ['txt', 'pdf', 'doc', 'html', 'docx', 'wps', 'odt']
ext_foto = ['png', 'jpg', 'jpeg', 'raw', 'gif', 'jpeg']
ext_video = ['mp4', 'avi', 'mkv', 'wmv', 'flv']
ext_audio = ['wav', 'mp3']
ext_rar = ['rar']
ext_exe = ['exe']

folders = [f.path for f in os.scandir(PATH) if f.is_dir()]
all_files = [f for f in os.listdir(PATH) if os.path.isfile(os.path.join(PATH, f))]

def move_files(type_f, path_file):
    global folders
    path_text = os.path.join(PATH, type_f)
    if not type_f in folders:
        os.mkdir(path_text)
        folders.append(type_f)
    shutil.move(path_file, path_text)

for file in all_files:
    print(file)

for file in all_files:
    path_file = os.path.join(PATH, file)
    file = file.split('.')
    if file[1] in ext_text:
        move_files('text', path_file)
    elif file[1] in ext_foto:
        move_files('foto', path_file)
    elif file[1] in ext_video:
        move_files('video', path_file)
    elif file[1] in ext_audio:
        move_files('audio', path_file)
    elif file[1] in ext_rar:
        move_files('rar', path_file)
    elif file[1] in ext_exe:
        move_files('exe', path_file)
    else:
        move_files('otros', path_file)
