import os

def dibujar(vidas, secret):
	os.system('clear')
	print('Vidas: ',' '.join(vidas))
	print(' '.join(secret))

def comprv_char(secret, key, char):
	restar_vida = False
	if char not in key:
		restar_vida = True
	for i in range(len(key)):
		if key[i] == char:
			secret[i] = key[i]
	return secret, restar_vida

def main():
	os.system('clear')
	vidas = ['<3' for i in range(6)]
	key = input('Introduce la palabra: ')
	secret = ['_' for i in key]
	while len(vidas) > 0:
		dibujar(vidas, secret)
		char = input("Introduce la letra: ")
		secret, restar_vida = comprv_char(secret, key, char)
		if char == key or ''.join(secret) == key:
			print("Has ganado")
			break
		if restar_vida:
			vidas = vidas[:-1]
	if len(vidas) < 0:
		print("Game Over")

main()
