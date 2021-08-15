import pandas as pd
import os

df = pd.read_csv('users.csv')

def login(user, passw):
	usr = df.loc[df['name'] == user]
	if usr.empty:
		print("No existe el usuario.")
		return False
	else:
		if usr['pin'][0] == passw:
			return True
		else:
			print("Pin incorrecto")
			return False

def register(user, passw):
	usr = df.loc[df['name'] == user]
	if usr.empty:
		os.mkdir(user)
		work_path = os.path.join(os.path.dirname(__file__), user)
		passw_file = open(os.path.join(work_path, '.passwd.txt'), 'w+')
		key = input("Introduce una clave para realizar la encriptacion: ")
		with open(os.path.join(work_path, '.key.key'), 'wb') as key_file:
			key_file.write(str.encode(key))
		print("Carpeta personal creada")
	else:
		print("El usuario ya existe")

register('bogdana', 12346)
