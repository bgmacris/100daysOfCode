import os
from time import sleep

os.system('clear')

f_inbox = ['B', 'U', 'G']
inbox = [-99, -99, -99, -99]
outbox = []

cajas_cen = {
	0: 'U',
	1: 'J',
	2: 'X',
	3: 'G',
	4: 'B',
	5: 'E'
}

print(inbox)
print(cajas_cen)

moves = ['inbox', 'outbox', ['copyfrom-', 'NUM']]
print(moves)

while outbox != f_inbox:
	mv = input("Movimiento (separados por comas): ")
	mv = mv.replace(' ', '').split(',')
	mv_e = []
	for i in mv:
		if i == moves[2][1]:
			i = i.split['-']
		mv_e.append(i)
	mv = mv_e
	for i in mv:
		if i in moves or i[:-1] in moves[2]:
			if i == moves[0]:
				get_caja = inbox.pop(0)
				print(f"Has cojido la caja {get_caja}")
			if i == moves[1]:
				put_caja = outbox.append(get_caja)
				print(f"Se ha dejado la caja {get_caja}")
			if i[:-1] == moves[2][0]:
				get_caja = cajas_cen[int(i[-1])]
				print(f"Has cojido la caja {get_caja}")
		sleep(0.5)
