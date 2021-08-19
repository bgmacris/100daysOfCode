import socket
import time

client = socket.socket()
ip = 'localhost'
port = 8888
client.connect((ip, port))

try:
	while True:
		cmd = input('FTP: ')
		client.send(cmd.encode('UTF-8'))
		cmd = cmd.split(' ')
		print(cmd)
		name_f = cmd[1].split('/')[-1]
		print(name_f)
		if cmd[0] == 'exit':
			client.send('exit'.encode('UTF-8'))
			client.close()
			break
		if 'get' in cmd:
			with open(name_f, 'wb') as f:
				while True:
					data = client.recv(1024)
					if data == b'EOF':
						print('OK')
						break
					f.write(data)
				print("Descarga realizada")
		if 'put' in cmd:
			print(f"Se esta passando el archivo {cmd[1]}")
			with open(cmd[1], 'rb') as f:
				while True:
					a = f.read(1024)
					if not a:
						break
					client.send(a)
				time.sleep(0.5)
				client.send('EOF'.encode())
				time.sleep(1)
				print("Archivo passado")
except:
	client.close()
