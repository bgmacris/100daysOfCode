import random

diccionario = {
    'abc_upper': [chr(i).upper() for i in range(ord('a'), ord('z')+1)]+['ñ'],
    'abc_lower': [chr(i) for i in range(ord('a'), ord('z')+1)]+['ñ'],
    'characters': [chr(i) for i in range(33, 48)],
    'nums': [i for i in range(10)]
}

while True:
    LENGHT = input("Que tamaño quieres que tenga la contraseña: ")
    try:
        LENGHT = int(LENGHT)
        break
    except:
        print("Introduce un numero. . .")

random_list = [random.choice(list(diccionario.keys())) for i in range(LENGHT)]    
password = ''.join([str(random.choice(diccionario[i])) for i in random_list])
print(password)
