import socket

IP = socket.gethostbyname(input("Introduce la IP que quieres escanear: "))

print("Escaneando . . .")
try:
    for port in range(1, 151):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((IP, port))
        if resultado == 0:
            print(f"El puerte {puerto} esta abierto.")
        s.close()
except:
    pass