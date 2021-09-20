"""
Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
"""

import pandas as pd

def gastos(datos, meses):
    datos['Balance'] = datos.Ventas - datos.Gastos
    return datos[datos.Mes.isin(meses)].Balance.sum()

datos = pd.DataFrame({
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [30500, 35600, 28300, 33900],
    'Gastos': [22000, 23400, 18100, 20700]
})
print(gastos(datos, ['Enero', 'Febrero']))
