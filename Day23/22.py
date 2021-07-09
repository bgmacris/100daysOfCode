'''
*Fecha y hora*
Imprimir la fecha y hora actuales.
'''

from datetime import datetime

hoy = datetime.now()
print("Fecha: " + str(hoy.strftime('%d/%m/%Y')) + '\nHora: ' + str(hoy.strftime('%Hh %Mmin')))