import socket
import time

server = socket.socket()
ip = 'localhost'
port = 8888
server.bind((ip, port))
server.listen(1)

user, addr = server.accept()
try:
	while True:
		cmd = user.recv(1024).decode('UTF-8')
		cmd = cmd.split(' ')
		if cmd[0] == 'exit':
			server.close()
			break
		if 'get' in cmd:
			print(f"Se esta passando el archivo {cmd[1]}")
			with open(cmd[1], 'rb') as f:
				while True:
					a = f.read(1024)
					if not a:
						break
					user.send(a)
				time.sleep(0.5)
				user.send('EOF'.encode())
				time.sleep(1)
				print("Archivo passado")
		if 'put' in cmd:
			name_f = cmd[1].split('/')[-1]
			with open(name_f, 'wb') as f:
				while True:
					data = user.recv(1024)
					if data == b'EOF':
						print('OK')
						break
					f.write(data)
				print("Descarga realizada")
except Exception as e:
	print("Exception", e)
	server.close()
