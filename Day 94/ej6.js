/**
Ejercicio 9
Crear un archivo con el nombre ej9.js
Levantar un servidor utilizando Express, el servidor tiene que responder con
el siguiente texto: 'Bienvenidos a Node.js Server Side'
Al levantar el servidor tiene que mostrar un mensaje que diga:
`Servidor corriendo en el puerto ${puerto}`. En caso de haber un error al levantar
el servidor tiene que mostrar el siguiente mensaje:
`No se pudo levantar el servidor en el puerto ${puerto}`
*/
const express = require('express');
const port = 5000;
const app = express();

app.get('/', (req, res) => {
    res.send("Bienvenidos a Node.js Server Side")
})

app.listen(port, (error) => {
    if (error) return console.log(`Error: ${error}`);
    console.log(`Servidor corriendo en el puerto ${port}`);
});