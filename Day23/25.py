'''
*Anagramas*
Crear una función que detecte si dos palabras son anagramas.
'''
from unidecode import unidecode

def anagrama(word1,word2):
    for i in list(unidecode(word1).lower()):
        if i in list(unidecode(word2).lower()) and len(word1) == len(word2):
            return 'True'
        else:
            return 'False'

print(anagrama(input(''),input('')))
