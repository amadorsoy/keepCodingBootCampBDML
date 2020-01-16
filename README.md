# Práctica Big Data Architecture

## Información general. 
Establecer una arquitectura en Google Cloud Platform que 

## Nombre del producto

## Descripción del producto
Recomendador de AirBnb por lifestyle (restaurantes guay, tiendas chulas...) esto es el ejemplo del profesor, yo prefiero buscar las zonas más tranquilas

## Estrategia del DAaaS
Voy a pasar un reporte mensual de los mejores 50 pisos para alquilar de airbnb en Madrid

## Arquitectura
Crawler con scrapy que lee de Yelp, los ficheros los meto en Hadoop, los junto con el dataset de airbnb (no se como) y hago un job de mapreduce para obtener
un top 50 en un archivo que luego enviare por correo

Todo irá a un cluster de hadoop en mi pc con windows y docker

## Operation Model
Hare todo a mano (realmente podemos hacer cosas con programación) y sacaré el reporte fial con un "copyToLocal" de hdfs y eso lo envío como un email a mano.

## Diagrama
Poner la url del diagrama de 

https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json
https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextchannel=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextfmt=default#

este es de las paradas de metro y guagua
https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=08055cde99be2410VgnVCM1000000b205a0aRCRD&

para crear la imagen
https://www.genial.ly/

para grabar el escritorio
https://hipertextual.com/2016/12/grabar-videos-windows-10-game-dvr

sdk google cloud porque se puede hacer todo por comandos


/*
# Practica BDA Demo

## Idea general

Coger datos de sitios web como yelp y recomendar apartamentos de airbnb cerca.

## Nombre del Producto

Recomendador de Airbnb por Lifestyle (restaurantes guay, tiendas chulas)

### Estrategia del DAaaS

Voy a pasar un reporte mensual de los mejores 50 pisos para alquilar de airbnb en 
Madrid. Utilizar herramientas en la nube para facilitar el manejo de los datos.

### Arquitectura

Arquitectura Cloud basada en Scrapy + Google Cloud Storage + HIVE + Dataproc
  
Crawler con scrapy que lee de Yelp, me escribe los resultados en csv. Y lo ejecuto 
en un Cloud Function.
  
Insertar el dataset de airbnb en HIVE. 
  
Tanto el resultado del scrap como el dataset de airbnb los colocare en un segmento de 
Google Cloud.
  
Desde Google Storage cogere los datos para crear 2 tablas de HIVE, y realizare 
una query con un JOIN que reste las distancias entre cada airbnb y los locales 
con mejores reviews.
  
De la query obtendre el TOP de apartamentos de airbnb de menos de 100 euros la noche. 
  
El resultado de la query estara en Google Storage.
  
### Operating Model

Hay un operador que soy yo, voy a disparar el cloud function todas las mananas con 
mi Google Home (le dire: "Ok Google crawlea yelp"). Esto disparara el cloud function 
y guardara el resultado en un directorio del segmento llamado "input_yelp".

En el segmento siempre habra un directorio llamado "input_airbnb".

Seguire el standard de levantar el Cluster solamente cuando quiera regenerar el TOP.

Una vez al dia, levantare el CLUSTER a mano, enviare las tareas de:  
- crear tabla de airbnb
- crear tabla de yelp
- load data inpath de gs://XXXX:input_yelp/ into table yelp
- load data inpath de gs://XXXX:input_airbnb/ into table airbnb
- SELECT JOIN INTO DIRECTORY 'gs://output/results'

Apago el cluster y me voy a dormir.

Voy a montar una web con un link directo al Google Storage Segment Object.

### Desarrollo

- Tengo el cloud function aqui: 
- Query de HIVE
- Pantallazo final


### Diagrama

https://docs.google.com/drawings/d/1PmTkZWffrCy3KSQ_Lq8n-jrmFqr4SbsllP5WDW64QuY/edit?usp=sharing


### Crawler

https://colab.research.google.com/drive/1U5mSOVMUL1w8lxhqCteKQYy9JNwtCuoc
*/