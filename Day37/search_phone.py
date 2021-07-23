import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from random import randint
import csv


def crear_numeros(inicio, moviles=True):
	process = 1000
	numeros = []
	while process:
		num = f"+34{inicio}" + ''.join([str(randint(0,9)) for i in range(8)])
		if num not in numeros:
			process = process - 1
			numeros.append(num)
	return numeros


numeros_moviles_6 = crear_numeros(6)
numeros_moviles_7 = crear_numeros(7)
numeros_fijos_8 = crear_numeros(8)
numeros_fijos_9 = crear_numeros(9)

refer = {
	0: 'Num movil 6',
	1: 'Num movil 7',
	2: 'Num fijo 8',
	3: 'Num fijo 9'
}

listas = [numeros_moviles_6, numeros_moviles_7, numeros_fijos_8, numeros_fijos_9]
for lista in listas:
	valid_num_count = 0
	with open(f"lista{listas.index(lista)}.csv", 'w', newline='') as file:
		spamwriter = csv.writer(file, delimiter=',', quotechar='|')
		for num in lista:
			mobileNum = phonenumbers.parse(num)

			valid_num = phonenumbers.is_valid_number(mobileNum)
			mobileNum = phonenumbers.parse(num)
			timeZone = timezone.time_zones_for_number(mobileNum)
			company = carrier.name_for_number(mobileNum, "en")
			geoloc = geocoder.description_for_number(mobileNum, "en")

			data = [num, valid_num,  timeZone, company, geoloc]
			if valid_num:
				valid_num_count = valid_num_count + 1
				spamwriter.writerow(data)
	print(refer[listas.index(lista)], 'Valid numbers from 1000:', valid_num_count)
