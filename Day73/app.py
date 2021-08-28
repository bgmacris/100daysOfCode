from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry("600x500")
ventana.title('py app')
ventana.resizable(width=False, height=False)

s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L', '11', 'bold'))

# Pestañas de la app
notebook = ttk.Notebook(ventana)

tab1 = tk.Frame(notebook, bg='#FFFFFF', width=600, height=500)
tab2 = tk.Frame(notebook, bg='#FFFFFF', width=600, height=500)

notebook.add(tab1, text="Agenda")
notebook.add(tab2, text="Personality")

# Encabezados api
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

def fill_empty(parent, row, column):
    empty = Label(parent,bg='white')
    empty.grid(row=row, column=column)
    return empty

def draw_conexion(estado, tab):
    try:
        if estado.status_code == 200:
            color = 'green'
            x = 'Ok'
        else:
            color = 'red'
            x = 'Error'
    except:
        color = 'red'
        x = 'Error'

    myCanvas = Canvas(tab, width=20, height=20, bg=color)
    myCanvas.grid(row=0, column=0, sticky='nsew')
    return x

import requests
from requests_html import HTMLSession
def get_conexion(url, login=None):
    try:
        if (not login):
            session = HTMLSession()
            response = session.get(url)
    except:
        response = None
    return response

# AGENDA TAB
import socket
import json
def set_conection():
    global buscar, client, run
    client = socket.socket()
    client.connect(('10.145.128.56', 8888))
    client.send('bogdan'.encode('UTF-8'))
    stores1 = client.recv(8192).decode('UTF-8')
    sleep(0.3)
    stores2 = client.recv(8192).decode('UTF-8')
    sleep(0.3)
    stores3 = client.recv(8192).decode('UTF-8')
    sleep(0.3)
    stores4 = client.recv(8192).decode('UTF-8')
    sleep(0.3)
    stores5 = client.recv(8192).decode('UTF-8')
    sleep(0.3)
    return stores1, stores2, stores3, stores4, stores5

def get_info_buscar(event=None):
    global cmd, conect_server
    cmd = buscar.get()
    if cmd != 'exit':
        client.send(cmd.encode('UTF-8'))
        client.send(cmd.encode('UTF-8'))
    else:
        print(cmd)
    buscar.delete(0, 'end')

url = "http://estoolsrv.luxgroup.net/agenda/sgh/stores.php"

response = get_conexion(url)
x = draw_conexion(response, tab1)
estado = Label(tab1, text=' <--> Estado conexion <--> ' + x, bg='white')
estado.grid(row=0, column=1)
fill_empty(tab1, 1, 0)

if response != None:
    text_buscar = Label(tab1, text='BUSCAR TIENDA: ')
    text_buscar.grid(row=2, column=0)
    buscar = Entry(tab1, bg='gray')
    buscar.grid(row=2, column=1, sticky='nsew')
    submit = Button(tab1, text='Buscar', command=get_info_buscar)
    submit.grid(row=2, column=2, sticky='nsew')
    fill_empty(tab1, 3, 0)

    encabezado = response.html.find('#example', first=True).text
    lista_enc = encabezado.split("\n")
    lista_enc.remove('Extension')
    lista_enc.remove('Address')
    lista_enc.remove('Schedule')

    tree = ttk.Treeview(tab1, columns=(lista_enc[0]))
    tree['show'] = 'headings'
    tree['columns'] = lista_enc[1:]
    for i in lista_enc[1:]:
        tree.column(i, width=98)
        tree.heading(i, text=str(i))

    stores1, stores2, stores3, stores4, stores5 = set_conection()
    print(stores1)
    print("\n")
    print(stores2)
    print("\n")
    print(stores3)
    print("\n")
    print(stores4)
    print("\n")
    print(stores5)


    tree.grid(row=4,column=0, columnspan=10)

notebook.grid(row=0, column=0, sticky="nw")
ventana.bind('<Return>', get_info_buscar)
ventana.mainloop()
