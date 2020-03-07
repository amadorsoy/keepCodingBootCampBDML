# Modulo Modern Exploration & Visualization - D3.js

## Ejercicio practico

Tomando los datos de los precios de airbnb:
- Crear un mapa con los barrios de la ciudad de Madrid y pintarlos por colores según el precio medio del alquiler en el barrio.
- Crear una gráfica que en el eje Y tenga el número de propiedades y en el eje X el número de habitaciones de un barrio (Se puede tomar un barrio  solo, pero sería recomendable que al hacer click en el mapa los datos de la gráfica cambien)

## Consideraciones

El ejercicio se realiza con los datos del archivo practica.json, sin embargo se ha modificado tal archivo, porque los datos del número de propiedades por número de habitaciones en los barrios que contenían datos, estaban mal, para que pudiera tener cierta lógica el gráfico es preciso cambiar algunos valores en cada uno de los array, ya que los anteriores valores de bedrooms en el array son (0, 1, 1, 1, 1) y deberían ser al menos (0, 1, 2, 3, 4).

## Entrega

Se muestra el mapa de los barrios de Madrid, los colores de los barrios están basados en sus importes promedio, los colores se corresponden a unos intervalos de importes, tomando el mayor valor 300€ tras revisar los datos.

Si situamos el cursor sobre cada uno de los barrios nos aparece un mensaje indicando el nombre del barrio y el precio promedio. Es un pequeño "tooltip" que nos ayudará a ver el importe por barrio.

Si hacemos clic en alguno de los barrios nos mostrará (para aquellos que posean información al respecto) una gráfica con el número de viviendas según el número de habitaciones por vivienda.

- Práctica HTML - JavaScript leyendo los datos del archivo practica.json. [Aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/tree/master/modernvisualization/htmljavascript)