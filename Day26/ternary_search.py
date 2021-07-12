lista = [1, 5, 10, 15, 20, 25, 30, 35]


def ternary_search(lista, key):
    left = 0
    right = len(lista) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if key == lista[mid1]:
            return key, mid1
        if key == lista[mid2]:
            return key, mid2
        
        if key < lista[mid1]:
            right = mid1 - 1
        elif key > lista[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return -1

print(ternary_search(lista, 30))