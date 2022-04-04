# Pasos para ejecutar la API
1. instalar las librerias que estan en el archivo requeriments.txt
2. crear una base de datos llamada rastreo
3. ejecutar el archivo de modelos para que se creen las tablas
4. crear un usuario en tu base de datos con los campos que existen.
5. usar el metodo create para crear vehiculos en el endpoint: `http://127.0.0.1:5000/api/create` el cual recibe los parametros de: `plates, lat, lon y user_id` enviar en formato form del postman o thunder client.
6. usar el metodo actualizar en el endpoint `http://127.0.0.1:5000/api/update/id` el cual recibe los parametros de: `plates, lat, lon y user_id` enviar en formato form del postman o thunder client, ademas de pasar el id del vehiculo en la url
7. usar el metodo eliminar en el endpoint `http://127.0.0.1:5000/api/delete/id` el cual debes de pasar por la url el id del vehiculo para eliminarlo.
8. Para ver cada efecto de los distintos endpoints se puede visualizar con la ruta: `http://127.0.0.1:5000/api/view` 
 
 ## Nota: para ejecutar la Api se debe de ejecutar el archivo app.py
 
 ### No logre agregar la autentificacion de usuario por cuestiones de tiempo sin embargo ya lo he implementado antes con JWT y tokens. Una disculpa y espero que esta api sirva de algo.
 
