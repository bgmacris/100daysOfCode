import tkinter

root = tkinter.Tk()
root.geometry("20x25")

pos_1 = tkinter.Button(root, text="1")
pos_2 = tkinter.Button(root, text="2")
pos_3 = tkinter.Button(root, text="3")
pos_4 = tkinter.Button(root, text="4")

pos_1.grid(row=0 , column=0, columnspan=5, sticky="we")
pos_2.grid(row=0 , column=5, columnspan=5, sticky="we")
pos_3.grid(row=0 , column=10, columnspan=5, sticky="we")
pos_4.grid(row=0 , column=15, columnspan=5, sticky="we")

root.mainloop()
