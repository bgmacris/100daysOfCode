"""
Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen
y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.
"""

import pandas as pd

def calc_notas(notas):
    notas = pd.Series(notas)
    calculo = pd.Series([
        notas.min(),
        notas.max(),
        notas.mean(),
        notas.std(),
    ], index=['Min', 'Max', 'Media', 'Desviacion tipica'])
    return calculo

notas = {
    'bogdan': 5,
    'juan': 7,
    'alberto': 9,
    'maria': 8
}


print(calc_notas(notas))
