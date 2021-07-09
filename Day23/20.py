'''
*Bisiesto*
Crear una función que dado un año diga si es bisiesto.
'''

año = int(input('Introduce un año: '))
comprovar = lambda año: 'Bisiesto' if año % 4 == 0 and (not(año % 100 == 0) or año % 400 == 0) else 'No bisiesto'
print(comprovar(año))
