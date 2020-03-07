# Modulo Modern Exploration & Visualization - D3.js

## Ejercicio practico
Tomando los datos de los precios de airbnb:
- Crear un mapa con los barrios de la ciudad de Madrid y pintarlos por colores según el precio medio del alquiler en el barrio.
- Crear una gráfica que en el eje Y tenga el número de propiedades y en el eje X el número de habitaciones de un barrio (Se puede tomar un barrio  solo, pero sería recomendable que al hacer click en el mapa los datos de la gráfica cambien)

## Consideraciones

El ejercicio se realiza con los datos del archivo practica.json, sin embargo se ha modificado tal archivo, porque los datos del número de propiedades por número de habitaciones en los barrios que contenían datos, estaban mal, para que pudiera tener cierta lógica el gráfico es preciso cambiar algunos valores en cada uno de los array, ya que los anteriores valores de bedrooms en el array son (0, 1, 1, 1, 1) y deberían ser al menos (0, 1, 2, 3, 4).

## Formatos de entrega

Se ha pretendido implementar la solución al ejercicio dentro de una plataforma web que contuviera un API que obutivera los datos de Google Cloud Platform y un entorno visual para poder mostrar el mapa y el resto de datos.

Sin embargo la generación del archivo de tipo GeoJSon no dibuja del todo bien el mapa, por lo que va a poder ver:

- Práctica HTML - JavaScript leyendo los datos del archivo practica.json. [Aquí]()