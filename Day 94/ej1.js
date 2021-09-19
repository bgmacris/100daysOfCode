/**
 * Ejercicio 1
Crear un archivo con el nombre ej1.js
Levantar un servidor de Express
Al llamar a localhost:3000/api/products se debe mostrar el siguiente JSON:
{
  descripcion: 'Productos',
  items: [
    { nombre: 'taza de Star Wars' , precio: 300},
    { nombre: 'FIFA 22 PS4' , precio: 1000},
    { nombre: 'Remera superheore' , precio: 100},
    { nombre: 'Bincha de Piñon fijo' , precio: 200},
    { nombre: 'Grande de Muzza' , precio: 120},
    { nombre: 'Botella de Fernet por 1 litro' , precio: 220}
  ]
}
 */

const express = require('express');

const app = express();
app.set('port', 3000);

app.get('/', (req, res) => {
    res.send("RUN");
});

app.get('/api', (req, res) => {
    res.json(
        {
            descripcion: 'Productos',
            items: [
                { nombre: 'taza de Star Wars', precio: 300 },
                { nombre: 'FIFA 22 PS4', precio: 1000 },
                { nombre: 'Remera superheore', precio: 100 },
                { nombre: 'Bincha de Piñon fijo', precio: 200 },
                { nombre: 'Grande de Muzza', precio: 120 },
                { nombre: 'Botella de Fernet por 1 litro', precio: 220 }
            ]
        }
    )
});

app.listen(app.get('port'), () => {
    console.log("Server port", app.get('port'));
});