"""
Buscar datos La Sénia
"""
from controller import Idescat

idescat = Idescat()

id_senia = idescat.get_id_pob('senia')
print(id_senia)

# Datos superficie
# datos_senia['gg']['g'][0]['tt']['t']['ff']['f']

# for i in datos_senia['gg']['g'][0]['tt']['t']['ff']['f']:
#     print(i)
