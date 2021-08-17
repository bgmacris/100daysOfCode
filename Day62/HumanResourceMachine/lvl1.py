import os
from time import sleep

os.system('clear')
f_inbox = [5, 9, 7]
inbox = [5, 9, 7]
outbox = []

print(inbox)

moves = ['inbox', 'outbox']
print("Movimientos", moves)
while outbox != f_inbox:
	mv = input("Movimiento (separados por comas): ")
	mv = mv.replace(' ', '').split(',')
	print(mv)
	for i in mv:
		if i in moves:
			if i == moves[0]:
				get_caja = inbox.pop(0)
				print(f"Has cojido la caja {get_caja}")
			if i == moves[1]:
				put_caja = outbox.append(get_caja)
				print(f"Se ha dejado la caja {get_caja}")
			sleep(0.5)
		else:
			print("No existen los comandos introducidos")
	if outbox != f_inbox:
		os.system('clear')
		print("Aun faltan comandos para realizar la tarea")
		inbox = [5, 9, 7]
		outbox = []
		print(inbox)

