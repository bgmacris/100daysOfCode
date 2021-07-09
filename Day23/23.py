'''
*Calendario*
Importar la librería calendar. Imprimir el calendario del mes actual.
'''

import calendar
import datetime

print(calendar.month(datetime.datetime.now().year, datetime.datetime.now().month))
