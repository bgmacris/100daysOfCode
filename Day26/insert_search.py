lista = [1, 5, 10, 15, 20, 25, 30, 35]


def search_inser(lista, key):
    left = 0
    right = len(lista) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if key > lista[mid]:
            left = mid + 1
        else:
            right = mid -1
    return left

print(search_inser(lista, 7))