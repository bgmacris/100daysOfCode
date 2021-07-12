lista = [1, 5, 10, 15, 20, 25, 30, 35]

def binary_search(lista, key):
    left = 0
    right = len(lista) - 1
    
    pasos = 0
    while left <= right:
        pasos = pasos + 1
        mid = (left + right) // 2
        if key > lista[mid]:
            left = mid + 1
        elif key == lista[mid]:
            print(pasos)
            return key, mid
        else:
            right = mid - 1
    
    print(pasos)
    return -1

print(binary_search(lista, 30))