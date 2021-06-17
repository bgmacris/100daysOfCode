"""
Buscar datos La Sénia
"""
from controller import Idescat

idescat = Idescat()

id_senia = idescat.get_id_pob('senia')
if 'id' in id_senia:
    id_senia = id_senia['id']
    datos_pob = idescat.get_info_pob(id_senia)
    print(datos_pob)
else:
    print("No se ha encontrado la poblacion")

# Datos superficie
# datos_senia['gg']['g'][0]['tt']['t']['ff']['f']

# for i in datos_senia['gg']['g'][0]['tt']['t']['ff']['f']:
#     print(i)
