'''
*Series*
Listar los números entre un valor inicial y uno final, con un cierto intervalo. Al final dar la suma de todos los valores listados.
'''


num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
intervalo = int(input("Intervalo: "))

# Utilizamos bucle for para crear la lista con los valores que nos a dado el usuario.
lista = [i for i in range(num1,num2 + 1,intervalo)]

print(lista)
print('Suma total: ' + str(sum(lista)))