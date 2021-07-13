"""
Sumar lista metodo recursivo
"""

def resursion_sum(lista):
    total = 0
    for i in lista:
        if type(i) == list:
            total = total + resursion_sum(i)
        else:
            total = total + i
            
    return total
            
if __name__ == "__main__":
    estado_inicial = [1, 2, [3, 4], [5, 6], [5, [5, 6]]]
    print(resursion_sum(estado_inicial))
