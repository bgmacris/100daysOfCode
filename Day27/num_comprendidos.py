"""
¿Cuáles y cuántos son los números primos comprendidos
entre 1 y 1000?
"""

def es_primo(num):
    comprv = True
    for i in range(2, num+1):
        if i != num and num % i == 0:
            comprv = False
            break
    return comprv

comprendidos = lambda limit: [i for i in range(2, limit) if es_primo(i)]
lista = comprendidos(1001)
print(lista)
print(f"Total numeros {len(lista)}")