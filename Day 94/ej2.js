/**
 * Ejercicio 2
Crear un archivo con el nombre ej2.js
Levantar un servidor de Express
Manejar las siguientes rutas:
Ruta: Raiz del sitio ,Metodo: get, Acción: Mostrar un mensaje de bienvenida
Ruta: Productos, Metodo: get, Acción: Mostrar un mensaje que diga: listado de
productos
Ruta: Productos, Metodo: post, Acción: Mostrar un mensaje que diga: crear
un producto
Ruta: Productos, Metodo: put, Acción: Mostrar un mensaje que diga: actualizar
un producto
Ruta: Productos, Metodo: delete, Acción: Mostrar un mensaje que diga: borrar
un producto
Ruta: Usuarios, Metodo: get, Acción: Mostrar un mensaje que diga: listado de
usuarios
Ruta: Usuarios, Metodo: post, Acción: Mostrar un mensaje que diga: crear un usuario
Ruta: Usuarios, Metodo: put, Acción: Mostrar un mensaje que diga: actualizar
un usuario
Ruta: Usuarios, Metodo: delete, Acción: Mostrar un mensaje que diga: borrar
un usuario
Crear un método que maneje todos los verbos de HTTP para la pagina
Utilizar Postman para probar todos los llamados
 */

const express = require('express');

const app = express();
app.set('port', 3000);

app.get('/', (req, res) => {
    res.send("Bienvenido");
});

app.get('/productos', (req, res) => {
    res.send("Listado de productos");
});

app.post('/productos', (req, res) => {
    res.send("Crear un producto");
});

app.put('/productos', (req, res) => {
    res.send("Actualizar un producto");
});

app.delete('/productos', (req, res) => {
    res.send("Borrar un producto");
});

app.listen(app.get('port'), (req, res) => {
    console.log("Server port", app.get('port'));
});
