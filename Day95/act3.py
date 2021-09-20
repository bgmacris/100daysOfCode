"""
Escribir una función que reciba una diccionario con las notas de los alumnos en curso
en un examen y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
"""

import pandas as pd

def aprovados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)


notas = {
    'carlos': 4,
    'pedro': 7,
    'monica': 3,
    'bogdan': 5,
    'juan': 7,
    'alberto': 9,
    'maria': 8
}

print(aprovados(notas))