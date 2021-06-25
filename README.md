<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>
  
  <h3 align="center">#100daysOfCode</h3>
</p>


<details open="open">
  <summary><h2 style="display: inline-block">Index</h2></summary>
  <ol>
    <li><a href="##1 day">1 Day</a></li>
    <li><a href="##2 day">2 Day</a></li>
    <li><a href="##3 day">3 Day</a></li>
    <li><a href="##4 day">4 Day</a></li>
    <li><a href="##5 day">5 Day</a></li>
    <li><a href="##6 day">6 Day</a></li>
    <li><a href="##7 day">7 Day</a></li>
    <li><a href="##8 day">8 Day</a></li>
    <li><a href="##9 day">9 Day</a></li>
  </ol>
</details>

## 1 Day

Invistigar funcionamiento API Idescat.cat
 ```sh
    https://www.idescat.cat/
 ```

# controller.py
Crear el objeto principal, donde se van a realizar todas las peticiones.
  * Obtener ID de una poblacion(poder buscarla)
  * Obtener Informacion de una poblacion, mediante su ID(Falta darte formato a la info)
  * Obtener todas las poblaciones

Requiriments:
  * flask

# main.py
Donde realiza la busqueda del apoblacion y su info


## 2 Day
Continuar trabajando con la api de Idescat.cat

Añadir funciones para interpretar la informacion que la API nos da sobre las poblaciones.
  * Datos de superficie/Densidad
  * Datos poblacion dividida por sexo
  * Datos poblacion dividida por edad
  * Datos poblacion dividida por edad Hombres
  * Datos poblacion dividida por edad Mujeres
  *  Datos poblacion dividida por lugar de nacimiento
  *   Datos poblacion dividida por nacionalidad


## 3 Day
Aplicacion tkinter con dos pestañas:
  * Primera pestaña: Bloc de notas
    ```sh
    Permite, crear, guardar abrir archivos
    ```
  * Segunda pestaña: Dejar de fumar(inacabada)
    ```sh
    De momento solo permite insertar i guardar datos
    ```
    
## 4 Day
Seguimiento dia 3, aplicacion tkinter.
  * Arreglo funciones de cargar/guardar datos
  * Arreglo posicionamiento elementos
  * Añadir calculo coste de cada cigarro, segun los datos del usuario

## 5 Day
Preparacion del entorno de trabajo de Django.
  * Confoguracion archivos conexion Base de datos
  * Configuracion estructura principal del proyecto
  * Creacion del login/logout

## 6 Day
Continuar con el proyecto Django, cambios realizados:
  * En las templates inicio-login
  * archivos css/js


## 7 Day
Algoritmo de calculos de rutas(conexiones establecidas)(Busqueda en aplietud)
archivo main para realizar la busqueda sin necesidad de la api.
api:
  */conexiones -> Devuelve las conexiones permitidas(json)
  */search/<data> -> (data = Ex: Malaga, sevilla) buscar la ruta mas corta
  
## 8 Day
Algoritmo de busquedada en amplietud, este algoritmo se encarga de resolver 
puzles formados por 4 piezas, cada movimiento solo puede intercambiar dos piezas
asi hasta llegar a la solucion del problema.

Ejemplo(Para entender el juego y como funciona los movimientos):
  * Estado Inicial = [4,3,2,1]
  * Solucion = [1,2,3,4]

    * Primer movimiento = [3,4,2,1] -> Se han intercambiado el 4 con el 3, y el resto a seguido igual
    * Segundo movimiento = [3,2,4,1] -> Se han intercambiado el 4 con el 2.
    * Tercer movimiento = [3,2,1,4] -> Se han intercambiado el 4 con el 1.

## Day 9
Servidor simple para un chat(grupal)
  * Para ejecutar el servidor -> python3 server.py localhost, 8080 (donde pone localhost se puede utilizar una ip, y puerte puedes poner el que quieras)
  * Para ejecutar los clientes -> python3 client.py localhost, 8080 (igual que arriba)
  * Solo puede ejecutar un servidor en el mismo puerto, y puedes connectar los clientes que quieras al servidor
  * Cuando alguien envia un mensaje se lo enviara a todos los otros connectados al server
