import tkinter as tk
from tkinter import filedialog
import csv
import shutil
import os
from tempfile import NamedTemporaryFile

app = tk.Tk()
app.title("Se stie")
app.geometry("160x50")

def UploadFile(event=None):
	filename = filedialog.askopenfilename()
	if filename != ():
		print('Selected:', filename)
		tempfile = NamedTemporaryFile("w+t", newline='', delete=False)
		modify = ["107", "407", " ", "'", "+"]
		with open(filename, newline='') as csvfile, tempfile:
			content = csv.reader(csvfile, delimiter=',', quotechar="|")
			writecontent = csv.writer(tempfile, delimiter=',', quotechar="|")
			for line in content:
				for i in modify:
					if i in line[4]:
						if i not in [" ", "'", "+"]:
							line[4] = line[4].replace(i, '07')
						else:
							line[4] = line[4].replace(i, '')
				writecontent.writerow(line)
			shutil.move(tempfile.name, filename)

upload = tk.Button(app, text="Modify File", command=UploadFile)
upload.pack()

app.mainloop()
