"""
Dia 1, #100DaysOfCode
Controlador de la api de https://www.idescat.cat/
"""

import requests

class Idescat:
    def __init__(self):
        self.data = "data"
        self.url = "https://api.idescat.cat/"


    def normalize(self, text):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        
        for a, b in replacements:
            text = text.replace(a, b).replace(a.upper(), b.upper())
        
        return text.upper()
    
    
    def transform_to_int(self, data, deci=False):
        # deci = decimal(float)
        if deci:
            data = float(data.split(',')[0])
        else:
            data = int(float(data.split(',')[0]))
        return data

    
    def transform_to_dict(self, dictt, especial=False):
        data = {}
        if especial:
            for i in dictt:
                data[i['c']] = {
                    i['u']: self.transform_to_int(i['v'], deci=True)
                }
        else:
            for i in dictt:
                data[i['c']] = {
                    'Habitantes': self.transform_to_int(i['v'], deci=True)
                }
        return data

    def get_id_pob(self, name):
        poblaciones = self.get_poblaciones()
        name = self.normalize(name)
        for i in poblaciones:
            content = self.normalize(i['content'])
            if name in content:
                data = {
                    'id': i['id'],
                    'name': i['content']
                }
                return(data)
                
    
    def get_info_pob(self, id):
        info = requests.get(self.url+f"emex/v1/dades.json?id={id}").json()
        return info
    
    
    def interprete_data(self, data, method):
        # Datos Superficie/Densidad
        if method == 'SUP':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][0]['ff']['f']
                datos_sup = self.transform_to_dict(data, especial=True)
                return datos_sup
            except Exception as e:
                return {'Error': e}

        # Poblacion por sexo
        if method == 'div_pob_sex':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][1]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por grupos de edad
        if method == 'div_group_edad':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][2]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por grupos de edad Hombres
        if method == 'div_group_edad_men':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][3]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por grupos de edad Mujeres
        if method == 'div_group_edad_woman':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][4]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
            
        # Poblacion por lugar de nacimiento
        if method == 'div_pob_born':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][5]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por nacionalidad
        if method == 'div_pob_nac':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][6]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por nacionalidad HOMBRES
        if method == 'div_pob_nac_men':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][7]['ff']['f']
                datos_habitantes = self.transform_to_dict(data)
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
        
        # Poblacion por nacionalidad MUJERES
        if method == 'div_pob_nac_woman':
            try:
                data = data['fitxes']['gg']['g'][1]['tt']['t'][7]['ff']['f']
                datos_habitantes = {}
                for i in data:
                    datos_habitantes[i['c']] = {
                        'Habitantes': self.transform_to_int(i['v'])
                    }
                return datos_habitantes
            except Exception as e:
                return {'Error': e}
            
    def get_poblaciones(self):
        content = requests.get(self.url+"emex/v1/dades.json", data={'lang': 'es'}).json()
        poblaciones = content['fitxes']['cols']['col']
        return poblaciones
