from flask import Flask
import json
import search


app = Flask(__name__)

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

@app.route('/conexiones')
def conexiones():
    conexiones = {
            'malaga': {'salamanca', 'madrid', 'barcelona'},
            'sevilla': {'santiago', 'madrid'},
            'granada': {'valencia'},
            'valencia': {'barcelona', 'granada'},
            'madrid': {'salamanca', 'sevilla', 'malaga', 'barcelona', 'santander'},
            'barcelona': {'zaragoza', 'santiago', 'madrid', 'malaga', 'valencia'},
            'salamanca': {'malaga', 'madrid'},
            'santiago': {'sevilla', 'santander', 'barcelona'},
            'santander': {'santiago', 'madrid'},
            'zaragoza': {'barcelona'}
        }

    return json.dumps(conexiones, default=set_default)


@app.route('/search/<data>')
def Search(data):
    data = data.split(',')
    print(data)
    inicio = data[0]
    objetivo = data[1]

    busqueda = search.search_ruta(inicio, objetivo)
    return json.dumps(busqueda)

if __name__ == '__main__':
    app.run()