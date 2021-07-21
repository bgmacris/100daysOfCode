import socket
import threading

def scan_port(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((host, port))
        server.close()
        return True
    except Exception as e:
        print(e)
        server.close()
        return False
    
open_ports = []
close_ports = []

host = '192.168.0.108'
for i in range(1,100):
    print(f"Scaneando puerto: {i}")
    if scan_port(host, i):
        open_ports.append(i)
    else:
        close_ports.append(i)

print("Open Ports", open_ports)
print("Close Ports", close_ports)
