import os
from time import sleep

os.system('clear')

f_inbox = ['L', 'O', 'A', 'D', 'P']
inbox = ['L', 'O', 'A', 'D', 'P']
outbox = []

comandos = ['-', 'jump', 'inbox', 'outbox']
print(comandos)
print("El '-' se utiliza junto al 'jump', lo que hace es crear un bucle retornando del 'jump' al '-'")
while outbox != f_inbox:
	mv = input("Movimiento (separados por comas): ")
	mv = mv.replace(' ', '').split(',')
	ejecutar = True
	for i in mv:
		if i not in comandos:
			print("Los comandos introducidos no son correctos")
			ejecutar = False
	if ejecutar:
		if 'jump' in mv:
			index__ = mv.index('-')
			index_j = mv.index('jump')
			mv = [mv[i] for i in range(len(mv)) if index__ < i < index_j]
			while outbox != f_inbox:
				for i in mv:
					if i in ['-', 'jump']:
						pass
					elif i == comandos[2]:
						get_caja = inbox.pop(0)
						print(f"Se ha cojido la caja {get_caja}")
					elif i == comandos[3]:
						outbox.append(get_caja)
						print(f"Se ha dejado la cja {get_caja}")
					sleep(0.5)
