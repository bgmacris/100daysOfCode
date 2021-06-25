import socket
import threading
import sys


class Server(object):
    def __init__(self, ip, port):
        try:
            self.server = socket.socket()
            self.server.bind((ip, int(port)))
            self.server.listen(2)
            
            self.clients = {}
            threading.Thread(target=self.listen).start()
        except Exception as e:
            print(e)
    
    def listen(self):
        while True:
            client, addr = self.server.accept()
            if addr not in self.clients:
                client.send('Introduce tu nombre de usuario: '.encode('UTF-8'))
                user = client.recv(1024).decode()
                self.clients[user] = client
                threading.Thread(target=self.Resend, args=(user,)).start()
            
    def Resend(self, client):
        while True:
            try:
                msg = self.clients[client].recv(1024).decode('UTF-8')
                if msg:
                    for i in self.clients:
                        if i != client:
                            print(msg)
                            self.clients[i].send(f'{client}: {msg}'.encode('UTF-8'))
            except:
                del self.clients[client]
                break


#Introducir IP servidor como argumento a la hora de ejecutar el script o como input si no se ha introducido anteriormente
if len(sys.argv) == 1: ip,port = input('Ip servidor: '), input('Puerto: ')
else: ip,port = sys.argv[1], sys.argv[2]

server = Server(ip,port)
