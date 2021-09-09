import os
import random

class bbdd:
    def __init__(self, file):
        self.file = os.path.join(os.path.dirname(__file__), file)

    def generator_key(self):
        large = random.randint(2, 15)
        return ''.join([chr(random.randint(50, 100)) for i in range(large)])

    def generator_data(self, file, count, info):
        if not info:
            columns = random.randint(4, 8)
            lines = []
        else:
            columns = info[columns]
            lines = info[name_col]
        for i in range(count):
            data = []
            for i in range(columns):
                data.append(self.generator_key())
            lines.append(data)
        for line in lines:
            line = ','.join(line)+'\n'
            file.write(line)
        file.close()

    def create_auto_data(self, action, count, info=False):
        if action == "CREAR":
            bbdd_w = open(self.file, 'w+')
            self.generator_data(bbdd_w, count, info)
        elif action == "APPEND":
            bbdd_a = open(self.file, 'a+')
            self.generator_data(bbdd_a, count, info)
        elif action == "VIEW":
            bbdd_r = open(self.file, 'r')
            lines = [line for line in bbdd_r]
            return lines
        else:
            return -1


BaseDatos = bbdd('bbdd.csv')
BaseDatos.create_auto_data('CREAR', 5)
BaseDatos.create_auto_data('APPEND', 5)
lines = BaseDatos.create_auto_data('VIEW', 0)
for i in lines:
    print(i)