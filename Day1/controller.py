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
        pass
    
            
    def get_poblaciones(self):
        content = requests.get(self.url+"emex/v1/dades.json", data={'lang': 'es'}).json()
        poblaciones = content['fitxes']['cols']['col']
        return poblaciones
