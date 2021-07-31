import os
import csv
from bbdd import DataBase


def menu(RUN):
	os.system('clear')
	print("Opciones: ")
	print("Crear base de datos - 1")
	print("Modificar base de datos - 2")
	print("Modificar datas de una base de datos - 3")
	print("Eliminar base de datos - 4")
	print("Exit - 99")
	while RUN:
		while True:
			command = input('Seleccione opcion: ')
			try:
				command = int(command)
				break
			except:
				print("La opcion tiene que ser un numero")
		if command == 99:
			RUN = False
		elif command == 1:
			name = input("Nombre de la base de datos: ")
			bbdd = DataBase(name)
			data = {}
			while True:
				print("Crea las columnas, indicando el nombre(Separado por comas)")
				columnas = input("")
				try:
					columns = columns.rename(' ', '')
					columnas = columnas.split(',')
					data['columns'] = columnas
					break
				except:
					print("Error de datos introducidos")
			bbdd.create_bbdd(name, data)

		break

RUN = True
menu(RUN)
