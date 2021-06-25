import socket
import threading
import sys

class Client(object):
    def __init__(self, ip, port):
        self.client = socket.socket()
        self.client.connect((ip, int(port)))
        
        msg = self.client.recv(1024).decode('UTF-8')
        print(msg)
        name = input("Name: ")
        self.client.send(name.encode('UTF-8'))
        
        threading.Thread(target=self.Send).start()
        threading.Thread(target=self.Recv).start()
    
    def Send(self):
        while True:
            try:
                self.client.send(input('').encode('UTF-8'))
            except:
                self.client.close()
                break
    
    # Recivir mensages( Bucle ejecutado en un hilo)
    def Recv(self):
        while True:
            try:
                msg = self.client.recv(1024).decode('UTF-8')
                print("\n" + msg)
            except:
                self.client.close()
                break
        
#Introducir IP servidor como argumento a la hora de ejecutar el script o como input si no se ha introducido anteriormente
if len(sys.argv) == 1: ip,port = input('Ip servidor: '), input('Puerto: ')
else: ip,port = sys.argv[1], sys.argv[2]

client = Client(ip,port)
