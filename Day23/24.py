'''
*Palídromos*
Dada una cadena decir si es un palíndromo.
'''

texto = input('').replace(' ', '').lower()

polindromo = lambda text: True if text == text[::-1] else False
print(polindromo(texto))

