# KeepCoding BootCamp Exploración y Visualización de Datos - Tableau

## Objetivo
El departamento comercial quiere captar la atención de la nueva ola de jovenes preocupados por el medio ambiente. Nos han pedido para empezar los barrios que mejor comunicados están vía Metro, para evitar tener que usar un coche y si es posible que además se pueda segmentar por los precios de los alojamientos, porque son jovenes y no necesariamente con recursos económicos. A través de los datos de AirBnb queremos indicar los lugares mejor comunicados vía Metro vamos a intentar plasmar en un pequeño dashboard los barrios mejor comunicados y que puedan resultar atractivos para el bolsillo.

Después de esta primera toma de contacto con la información, ya el departamento comercial se pondrá en contacto de nuevo para profundizar en más aspectos que puedan interesar.

## Origen de los datos
Para la práctica se hace uso de los datos de AirBnb y además se agregan los datos de las paradas del metro de Madrid. En la práctica de Arquitectura con Ricardo, obtuvimos diferentes datos, en mi caso obtuve los datos abiertos ofrecidos por la Comunidad de Madrid y el Ayutamiento a través de sus API.

El desarrollo de la descarga de los datos a través de la plataforma de Google Cloud y sus herramientas se puede visualizar en el ejercicio de la practica correspondiente a Arquitectura, que podrá encontrar [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/tree/master/bigdataarchitecture). 

Además dejo en el directorio de datos, los csv siguientes:

* Los datos obtenidos de la consulta directamente de Google Cloud Platform SQL (con postgresql como opción) [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/visualizaciondatostableau/datos/DatosAirBnBMadridConParadasMetroDeGooglePlatformSQL.csv).
* Los datos de las paradas de Metro de Madrid con su Geolocalización [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/visualizaciondatostableau/datos/metro.csv).


## ETL - Preparación de los datos

Una vez decididos los datos a usar, había que alojarlos en la plataforma de Google en la nube. Para eso seguí los siguientes pasos:

1. Limpieza de los archivos CSV: antes de subir los archivos había que "pulir" los registros, ya que en el proceso de carga de los datos, es necesario eliminar el "ruido" previamente o de lo contrario da error y no realiza la carga. Entre otras tareas hay que quitar todos los retorno de carro que existen en los String (los que van entre comillas). También hubo que eliminar algunos carácteres raros que podían complicar la carga.

2. Una vez hemos dejado los archivos lo más pulidos posible, subimos los archivos al servicio de Storage de Google Cloud Platform. Este proceso se realiza manualmente.

3. Para trabajar con los datos escogemos el servicio de SQL de GCP, se creó un servidor de PostGreSQL para alojar los datos y posteriormente realizar las sentencias SQL necesarias para obtener unos datos con los que podamos empezar a trabajar. Podemos ver en la siguiente imagen el uso reciente del servidor PostGreSQL.
![Servidor PostGreSQL Google Cloud Platform](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/visualizaciondatostableau/imagenes/ServidorPostGreSQLGoogleCloudPlatform.PNG)

4. A través de la consola de GCP utilizamos el comando gsutil para copiar los archivos del Storage al servidor donde está alojada la instancia de PostGreSQL:
    ```
    gsutil cp gs://ismalp-bda5-keepcoding/inputdatamadrid/metro.csv ./metro.csv
    ```

5. Creamos la estructura necesaria para alojar los datos, podrá ver la estructura de las tablas [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/visualizaciondatostableau/estructura/tablas.sql).

6. De nuevo a través de la consola GCP y el entorno de trabajo de PostGreSQL, realizamos la carga de los datos, desde los archivos CSV a las tablas generadas anteriormente:
    ```
    \copy metromadrid FROM '/home/amadorsoy/metro.csv' DELIMITER ';' CSV HEADER;
    ```

7. Una vez tenemos los datos hemos realizado algunos cambios y hemos limpiado algunos registros para poder obtener una estructura más manejable con datos más consistentes:

    * Lo primero pasar los datos brutos de Airbnb a una estructura más reducida con los mismos registros, pero con menos columnas que puedieran distraernos o entorpecernos en el tratamiento de los datos.

    * Luego limpieza de datos, eliminación de todos aquellos registros que no fueran de Madrid o de la Comunidad de Madrid. Además de completar algunos campos que faltaban y que nos iban a ayudar en la posterior visualización. Convertir los datos de Latitud y Longitud a datos decimal con los que poder trabajar sin necesidad de hacer ningún "cast" en las sentencias SQL.

    * Rellenar una tabla con los datos de las distancias de los registros de AirBnb con las paradas de Metro.

    * Eliminar todos aquellos registros que tengan una distancia superior a 1.

    * Ejecutar la anidación que necesitamos para poder obtener los datos:
    ```
    Select airbnb.*, coalesce(paradas.nparadas, 0) as NParadas
    from airbnb
        left join (
                    select id, count(nombre) as nparadas
                    from airbnbmetro
                    group by id
        ) as paradas on paradas.id = airbnb.id
    ```
    * Descargamos los datos en un archivo CSV para evitar problemas de Conexión ya que tengo filtrada la IP y no abierto a todo el público. Para poder verlos hay que ir [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/visualizaciondatostableau/datos/DatosAirBnBMadridConParadasMetroDeGooglePlatformSQL.csv).

8. Ya con los datos en Tableau, hacer algunas modificaciones para poder tener los datos más "limpios".

    * Campo Calculado:
        * Barrio: IfNull( [neighbourhood], [neighbourhood_cleansed])
        
    * Cambio de Nombre:
        * ParadasMetro: campo nparadas
    
    * Ocultar campos:
        * Metro: finalmente un campo que no se usa para nada.
        * nparadas: nos quedaremos con el campo calculado ParadasMetro
        * neighbourhood: ya usamos el campo Barrio
        * neighbourhood_cleansed: ya usamos el campo Barrio


## DashBoard

Se crea un pequeño dashboard de visualización de los datos en el que puedan saber los barrios de Madrid mejor comunicados con el Metro y además saber cual es su franja económica.

La visualización está compuesta por una gráfica de barras y por un mapa. Ambos son interactivos, en primer lugar ambos dependen de los filtros facilitados a la derecha para poder aumentar o disminuir los baremos y así encontrar los barrios más atractivos para los jóvenes preocupados por el medio ambiente.

Además al mapa se le ha dado cierto nivel de detalle para que sin ser muy pesado ver los datos, se puedan hacer una idea exacta de la situación en la ciudad.

El archivo lo puede encontrar [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/tree/master/visualizaciondatostableau/LibroTrabajo).