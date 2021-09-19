/*
Crear un archivo index.js
Leer la documentación del módulo para aprender a usarlo
Instalar el módulo one-liner-joke
Configurar el proyecto para que al correr npm start corra el código del archivo
index.js. Mostrar en consola un chiste random. Mostrar en consola las categoría
a las que pertenece. Nota de color:

el método getRandomJoke retorna un objeto que tiene una propiedad body con el chiste
y la propiedad tags con las categorías
 */
const oneLinerJoke = require('one-liner-joke');

var chiste = oneLinerJoke.getRandomJoke();
console.log(`Chiste: ${chiste['body']}\nCategorias: ${chiste['tags']}`)