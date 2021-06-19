import os
import json
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as f
from functools import partial


app = tk.Tk()
app.title("Game Over")
app.geometry("450x500")
app.resizable(width=False, height=False)

s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L', '11', 'bold'))

notebook = ttk.Notebook(app)

tab1 = tk.Frame(notebook, bg='#FFFFFF', width=448, height=470)
tab2 = tk.Frame(notebook, bg='black', width=448, height=470)

notebook.add(tab1, text="Note")
notebook.add(tab2, text="No Fumes")

# NOTES TAB
url_file = ""
grindBox = 1


def write_file(conttent="", url=""):
    global url_file
    if not conttent:
        content = text.get(1.0, "end-1c")
    else:
        content = conttent
    # url_file = url
    file = open(url_file, "w+", encoding="utf-8")
    file.write(str(content))
    file.close()


def red_file():
    file = open(url_file, "r", encoding='utf-8')
    content = file.read()
    text.delete(1.0, "end")
    text.insert('insert', content)
    file.close()


def new_file():
    global url_file
    try:
        grindBox = 1
        salidaPy.grid_forget()
        scrollLabel.grid_forget()
    except:
        pass
    text.delete(1.0, "end")
    url_file = ""


def open_file():
    global url_file, salidaPy
    try:
        grindBox = 1
        salidaPy.grid_forget()
        scrollLabel.grid_forget()
    except:
        pass
    url_file = f.askopenfilename(initialdir='C:\\Users\\Bogdan\\Desktop\\pyapps\\tkinter\\book', filetype=(
        ("Archivo de Texto", "*.txt"), ("Archivos Python", "*.py"),), title="Abrir Archivo")
    if url_file != "":
        red_file()


def save_file():
    global url_file, salidaPy
    if not url_file:
        file = f.asksaveasfile(
            title="Save File", mode="w", defaultextension=".txt")
        if file is not None:
            url_file = file.name
            write_file()
        else:
            url_file = ""
    else:
        write_file()


botonNew = tk.Button(tab1, text="Nuevo Archivo", command=new_file)
botonOpen = tk.Button(tab1, text="Abrir Archivo", command=open_file)
botonSave = tk.Button(tab1, text="Guardar Archivo", command=save_file)
botonNew.grid(row=0, column=0, columnspan=1, sticky="we")
botonOpen.grid(row=0, column=1, columnspan=1, sticky="we")
botonSave.grid(row=0, column=2, columnspan=1, sticky="we")

scrollText = Scrollbar(tab1, width=20)
scrollText.grid(row=2, column=3, sticky="ns")
text = Text(tab1, bg='#CFCBCB', width=60, height=27,
            yscrollcommand=scrollText.set, font="Arial 10")
textcmd = ""
salidaPy = Label(tab1, text=textcmd)
scrollText.config(command=text.yview)
text.grid(row=2, column=0, columnspan=3, rowspan=1)

# No fumes tab
def cargar_datos():
    with open('data.txt') as json_file:
        data = json.load(json_file)

        nombre.set(i['name'])
        edad.set(i['edad'])
        cigarrosDia.set(i['cigarros_dia'])
        añosFumando.set(i['años_fumando'])
        que_fumas.set(i['que_fumas'])

def guardar_datos():
    if ',' in queFumas.get():
        que_fumas = queFumas.get().split(',')
    else:
        que_fumas = queFumas.get()
        
    data = {
        'name': nombre.get(),
        'edad': edad.get(),
        'cigarros_dia': cigarrosDia.get(),
        'años_fumando': añosFumando.get(),
        'que_fumas': que_fumas
    }
    print(data)
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    
botonCarga = tk.Button(tab2, text="Cargar Datos", command=cargar_datos)
botonGuardar = tk.Button(tab2, text="Guardar Datos", command=guardar_datos)
botonCarga.grid(row=0, column=0, columnspan=1, sticky="we")
botonGuardar.grid(row=0, column=1, columnspan=1, sticky="we")


etiquetaName = tk.Label(tab2, text="Nombre", bg="gray", textvariable='')
nombre = tk.Entry(tab2)

etiquetaEdad = tk.Label(tab2, text="Edad", bg="gray", textvariable='')
edad = tk.Entry(tab2)

etiquetaCigarrosDia = tk.Label(tab2, text="Cigarros al dia", bg="gray", textvariable='')
cigarrosDia = tk.Entry(tab2)

etiquetaAñosFumando = tk.Label(tab2, text="Años fumando", bg="gray", textvariable='')
añosFumando = tk.Entry(tab2)

etiquetaQueFumas = tk.Label(tab2, text="Que fumas", bg="gray", textvariable='')
queFumas = tk.Entry(tab2)

etiquetaName.grid(row=1, column=0, columnspan=1)
nombre.grid(row=1, column=1, columnspan=2)

etiquetaEdad.grid(row=2, column=0, columnspan=1)
edad.grid(row=2, column=1, columnspan=2)

etiquetaCigarrosDia.grid(row=3, column=0, columnspan=1)
cigarrosDia.grid(row=3, column=1, columnspan=2)

etiquetaAñosFumando.grid(row=4, column=0, columnspan=1)
añosFumando.grid(row=4, column=1, columnspan=2)

etiquetaQueFumas.grid(row=5, column=0, columnspan=1)
queFumas.grid(row=5, column=1, columnspan=2)


notebook.grid(row=0, column=0, sticky="nw")
app.mainloop()
