import tkinter as tk
from time import strftime


root = tk.Tk()
root.title("Digital-Clock")
root.resizable(width=False, height=False)
canvas = tk.Canvas(root, height=140, width=400)
canvas.pack()

frame = tk.Frame(root, bg='black')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
lbl = tk.Label(frame, font=('Helvetica', 30, 'bold'),
               background='white', foreground='black')
lbl.pack(anchor="s")


def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


time()

menubar = tk.Menu(root)
root.mainloop()
