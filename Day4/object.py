import json


class Salud:
    def __init__(self, name, edad, cigarros_dia, años_fumando, que_fumas):
        self.name = name
        self.edad = edad
        self.cigarros_dia = cigarros_dia
        self.años_fumando = años_fumando
        self.que_fumas = que_fumas

    def load_data(self):
        with open('data.txt') as json_file:
            data = json.load(json_file)
            if data:
                for i in data:
                    self.name = i['name']
                    self.edad = i['edad']
                    self.cigarros_dia = i['cigarros_dia']
                    self.años_fumando = i['años_fumando']
                    self.que_fumas = i['que_fumas']
                
