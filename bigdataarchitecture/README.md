# KeepCoding BootCamp Big Data Architecture Practical Exercise

# DataLake - BigData Architecture Practical Exercise

## Contextualizar. 

Debido a la creciente sensibilización de los consumidores con el cambio climático, el departamento de marketing ha propuesto establecer las viviendas que más ayudarían a respetar el planeta, para ello usamos los datos de Madrid ofrecidos por Airbnb y los unimos a los obtenidos usando el API del Ayuntamiento de Madrid que nos aporta la localización de las paradas de metro, además del listado de colegios públicos, principales parques, centros médicos y mercados municipales.

Una vez tengamos los ficheros, se cargan para su procesado. Se establece un sistema de puntos según los servicios que tenga la vivienda en menos de 500 metros, podemos ver el baremo:
- 3 puntos por cada dos paradas de metro
- 3 puntos por cada mercado municipal
- 4 puntos por cada parque o jardín
- 3 puntos por cada centro médico
- 3 puntos por cada colegio público

El resultado serán los 100 mejores resultados de la lista.

## Nombre del producto

Life in Madrid Like Greta, respeta el planeta.


## Descripción del producto

"Life in Madrid Like Greta, respeta el planeta." es un producto que va a ser promocionado a nivel Europa para ayudar a respetar un poco más el planeta a todos aquellos que están buscando casa en Madrid. Cuando mayor puntuación tenga la vivienda más servicios y más cercanos tiene que ayudan a no contaminar.


## Estrategia del DAaaS

Generar un archivo en formato csv con los 100 pisos de AirBnb en Madrid que más ayudarían a vivir sin contaminar para que el departamento de Marketing decida como va a querer dar uso de estos datos. Debido a la falta de infraestructura en local, se va a usar las herramientas que ofrece Google Cloud Platform en la "nube". Desde la descarga de los recursos, el procesado de los datos y la generación del archivo final tendrá lugar en Google Cloud Platform, teniendo acceso desde el departamento que necesita leer los resultados al path correspondiente del Storage de Google.


## Arquitectura

Estructura de Google Cloud Platform usada:
- Storage: se usará un Bucket especifico donde se descargarán primero los archivos necesarios para el estudio y donde se dejarán posteriormente los resultados.
    - Bucket: ismalp-bda5-keepcoding
        - Download Path to process: inputdatamadrid
        - Uplad Path to process: outputdatamadrid
        - Scripts path to process in DataProc Cluster: scripts
            - Script 1:
                - Nombre: installrequirements.sh
                - Descripción: instala dependencias, copia a local un script de python y lo ejecuta
                - URL: [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/googlecloudapp/GoogleCloudPlatform/scripts/installrequirements.sh)
            - Script 2:
                - Nombre: createtablesandloaddata.py
                - Descripción: lee los ficheros csv descargados y los transforma en las tablas necesarias para obtener los datos
                - URL: [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/googlecloudapp/GoogleCloudPlatform/scripts/createtablesandloaddata.py)

- Cloud Scheduler: trabajos programados que se ejecutarán cada domingo para descargar los ficheros primero y para procesarlos después.
    - KeepCoding Download Madrid Data: 
        - Schedule: cada domingo a las 5:00
        - Destino: HTTP
        - Metodo: GET        
        - Destino: La URL Generada por la cloud function download data.
    - KeepCoding Process Madrid Data:
        - Schedule: cada lunes a las 8:00
        - Destino: HTTP de App Engine
        - Metodo: POST
        - URL: /v1/projects/rock-sublime-264620/regions/europe-west1/clusters/
        - Cuerpo: [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/googlecloudapp/OtherCode/cluster.create.txt)
- Cloud Functions: llamadas por los trabajos programados se encargarán de realizar las acciones necesarias para obtener los resultados, en principio el lenguaje de programación seleccionado es Python para su configuración.
    - Cloud Function Download Data:
        - URL: [aquí](https://github.com/amadorsoy/bigdataarchitectkc/blob/master/googlecloudapp/GoogleCloudPlatform/functions/download-api-madrid.py)
- Clusteres DataProc: maquinas que se crearán y se usarán para procesar los datos y que posteriormente se eliminarán al finalizar el trabajo.
    - Code to create Cluster:
        - Estructura del Cluster: [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/googlecloudapp/OtherCode/cluster.create.txt)
        - Desarrollo:
            - Levantar un cluster DataProc
                - Instalar las dependencias necesarias
                    - Funciones: instalar tanto las librerías de Hive en Debian, como los módulos de python necesarios
                    - Script: installrequirements.sh visto anteriormente en la sección de Scripts
                    - Estado: completo, funciona correctamente
                - Ejecutar un script para ejecutar comandos en Hive:
                    - Funciones:
                        - Creación de estructura de datos
                        - Ejecución de sentencias SQL
                        - Exportación de datos resultantes
                    - Script: createtablesandloaddata.py visto anteriormente en la sección de Scripts
                    Estado: al 70% aproximadamente (puede que más), queda realizar el cálculo de la distancia, obtener la lista de los 100 mejores y exportar los resultados a un archivo csv en el bucket de Google Storage.


## Operation Model

Estructura desatendida en la descarga y procesado de datos:
1. Trabajo programado cada domingo a las 5:00: KeepCoding Download Madrid Data.
2. Ejecución de la descarga de los datos: Cloud Function Download Data
3. Trabajo programado cada domingo a las 6:00: KeepCoding Process Madrid Data
4. Creación de cluster, creación de la estructura de datos necesaria, procesar los datos y exportar los resultados a Google Storage.
5. El departamento que necesita los datos se descargará el archivo csv resultante para su análisis.

Hasta que no se tengan instrucciones de como mostrar los datos solo se dejarán los resultados en el Storage para que el departamento correspondiente lo pueda descargar y analizar. Cuando se tengan las instrucciones necesarias, se cambiará el destino de los resultados por la infraestructura necesaria.


## Diagrama
Para visualizar el diagrama [aquí](https://view.genial.ly/5e22fde1134c1a7009e3125b/interactive-content-keepcodingbda5-proceso)


## Fuentes de datos

### Datos AirBnB
Listado de los datos de Madrid: [aquí](https://public.opendatasoft.com/explore/dataset/airbnb-listings/export/?disjunctive.host_verifications&disjunctive.amenities&disjunctive.features&q=Madrid&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQ09VTlQiLCJ5QXhpcyI6Imhvc3RfbGlzdGluZ3NfY291bnQiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiJyYW5nZS1jdXN0b20ifV0sInhBeGlzIjoiY2l0eSIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6IiIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJyb29tX3R5cGUiLCJjb25maWciOnsiZGF0YXNldCI6ImFpcmJuYi1saXN0aW5ncyIsIm9wdGlvbnMiOnsiZGlzanVuY3RpdmUuaG9zdF92ZXJpZmljYXRpb25zIjp0cnVlLCJkaXNqdW5jdGl2ZS5hbWVuaXRpZXMiOnRydWUsImRpc2p1bmN0aXZlLmZlYXR1cmVzIjp0cnVlfX19XSwidGltZXNjYWxlIjoiIiwiZGlzcGxheUxlZ2VuZCI6dHJ1ZSwiYWxpZ25Nb250aCI6dHJ1ZX0%3D&location=16,41.38377,2.15774&basemap=jawg.streets)

### API de Madrid
Listado de fuentes de datos abiertos [aquí](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json)

Listado de paradas de metro, bus, tren [aquí](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=08055cde99be2410VgnVCM1000000b205a0aRCRD&)
