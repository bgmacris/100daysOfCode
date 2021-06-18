"""
Buscar datos La Sénia
"""
from controller import Idescat

# Crear el objeto para poder trabajar con las funciones
idescat = Idescat()

# Ejemplo buscar una poblacion
id_senia = idescat.get_id_pob('senia')
if 'id' in id_senia:
    # Extrar ID de la poblacion
    id_senia = id_senia['id']
    
    # Extraer todos los datos de la poblacion
    datos_pob = idescat.get_info_pob(id_senia)
    
    # Filtar datos de los datos extraidos(Superficie/Densidad)
    datos_superficie = idescat.interprete_data(datos_pob, method='SUP')
    print(datos_superficie, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por sexo)
    datos_habitantes_sex = idescat.interprete_data(datos_pob, method='div_pob_sex')
    print(datos_habitantes_sex, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por grupos de edad)
    datos_habitantes_edad = idescat.interprete_data(datos_pob, method='div_group_edad')
    print(datos_habitantes_edad, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por grupos de edad HOMBRES)
    datos_habitantes_edad_men = idescat.interprete_data(datos_pob, method='div_group_edad_men')
    print(datos_habitantes_edad_men, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por grupos de edad MUJERES)
    datos_habitantes_edad_woman = idescat.interprete_data(datos_pob, method='div_group_edad_woman')
    print(datos_habitantes_edad_woman, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por lugar nacimiento)
    datos_lugar_nacimiento = idescat.interprete_data(datos_pob, method='div_pob_born')
    print(datos_lugar_nacimiento, "\n")
    
    # Filtar datos de los datos extraidos(Poblacion por nacionalidad)
    datos_nacionalidad = idescat.interprete_data(datos_pob, method='div_pob_nac')
    print(datos_nacionalidad, "\n")
else:
    print("No se ha encontrado la poblacion")

# Datos superficie
# datos_senia['gg']['g'][0]['tt']['t']['ff']['f']

# for i in datos_senia['gg']['g'][0]['tt']['t']['ff']['f']:
#     print(i)
