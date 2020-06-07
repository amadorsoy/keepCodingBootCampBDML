# Machine Learning

## Archivo ipynb para Descarga
El ejercicio lo puede descargar [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/machinelearning/Pr%C3%A1ctica%20Machine%20Learning%20Amador%20L%C3%B3pez%20Parra.ipynb)

## Descripción del trabajo a realizar

Es un problema de regresión: hay que predecir el precio del airbnb utilizando los datos disponibles.

### Observaciones

En el trabajo se va a observar una sección de definición de funciones que se usan en varios puntos (así se reduce la duplicación de código).

También se crean algunas constantes para ayudar en la legibilidad del código.

Se decide usar RandomForestRegresor con GridSearchCV para la elección de las variables y para el primer cálculo de predicción con los datos. Ya que de esta forma, se espera filtrar las variables más destacadas y a partir de esta selección poder depurar la selección de variables y comparar luego con otros modelos para ver la mejor opción (siempre bajo el estudio que se realiza).

## Obtención de Datos

Se carga el archivo CSV que se indica en la constante en un DataFrame de pandas.

### Separar los datos de TRAIN y TEST

Se guardan los datos separados en archivos csv para asegurar tanto la salvaguarda, como el posible error en el uso.

Lo primero es cargar los datos de "TRAIN", todo se hará a partir de estos datos y se aplicará posteriormente a los de "TEST".


## Análisis Exploratorio y Preprocesamiento

### Analizar los datos según su ciudad

Se usa la variable "City" para visualizar y analizar los datos que hay en el archivo. Se obtienen los siguientes resultados:
- Registros totales: 11.824
- Registros de la ciudad de Madrid: 10.567
- Registros que no son de la ciudad de Madrid: 1.257

### Selección de datos de ciudad Madrid

Como se aplicará a los datos (train y test) los mismos procesos, para todos aquellos datos que entren que no sean de Madrid no se va a ofrecer un precio estimado.

- Se eliminan todos los registros que no son de la ciudad de Madrid.
- Al tener registros solo de la ciudad de Madrid, se pueden eliminar las siguientes variables que indican algo del territorio:
  - State
  - Country Code
  - Smart Location
  - Country
  - City

### Columnas sin valores

Se buscan las columnas sin registros en los datos de TRAIN, las guardamos en una variable y en caso que tengamos columnas sin datos, las eliminamos del DataFrame.


### Columnas que apreciamos no nos aportan ningún valor para el cálculo del precio

Tras sacar la lista de variables que habría que categorizar, lo primero que podemos ver es que hay variables que a priori no van a aportar ningún valor al cálculo del precio (entendamos registro por vivienda):
- Calendar Update: fecha de última actualización de los datos del registro
- Calendar last Scraped: última fecha de obtención de datos del registro
- First Review: primera vez que se visualizó el registro
- Last Review: última vez que se visualizó el registro
- Listing Url: el enlace del registro
- Last Scraped: última fecha de obtención de datos del registro
- Name: el nombre del registro
- Symmary: el resumen del registro
- Space: un texto indicativo de la ubicación del registro
- Description: un texto descriptivo del registro
- Neighborhood Overview: un texto descriptivo del barrio del registro
- Notes: observaciones del registro
- Transit: un texto descriptivo del tránsito del registro
- Access: texto de datos de acceso y otras particularidades
- Interaction: texto de datos de interacción con el propietario
- House Rules: texto con las reglas del registro
- Thumbnail Url: el enlace de la miniatura de la imagen del registro
- Medium Url: el enlace de tamaño medio de la imagen del registro
- Picture Url: el enlace a tamaño normal de la imagen del registro
- XL Picture Url: el enlace a tamaño grande de la imagen del registro
- Host URL: un enlace más del registro
- Host Name: el nombre de contacto del registro
- Host Since: la fecha desde que está el registro
- Host Location: dónde está ubicado el registro (no hace falta por el filtro de Madrid)
- Host About: texto del propietario
- Host Thumbnail Url: una miniatura de la imagen del propietario
- Host Picture Url: el enlace a la imagen del propietario a tamaño normal
- Amenities: un texto con cosas a favor del registro
- License: el identificador de licencia del registro

Tras observar las columnas que tienen valores NA o Nulo, vemos que hay dos columnas que no aportan al cálculo del precio:
- Weekly Price
- Monthly Price
- Host ID: el identificador del propietario
- ID: el identificador del registro
- Scrape Id: el identificador de la extracción de datos
- Geolocation: teniendo longitud y latitud, este campo debería sobrar.

### Columnas con valores nulos

El siguiente paso es verificar qué variables tienen datos nulos o NAN. 

```
Price                              8
Security Deposit                6018
Cleaning Fee                    4285
Review Scores Rating            2286
Review Scores Accuracy          2302
Review Scores Cleanliness       2297
Review Scores Checkin           2308
Review Scores Communication     2298
Review Scores Location          2311
Review Scores Value             2310
Reviews per Month               2179
Host Response Rate              1313
Host Listings Count                3
Host Total Listings Count          3
Bathrooms                         40
Bedrooms                          18
Beds                              37
Square Feet                    10154
```



Se puede apreciar un conjunto de variables con valores nulos con una transformación lógica:
- Review Scores Rating
- Review Scores Accuracy
- Review Scores Cleanliness
- Review Scores Checkin
- Review Scores Communication
- Review Scores Location
- Review Scores Value
- Reviews per Month
- Security Deposit
- Cleaning Fee
- Host Response Rate
- Host Listings Count
- Host Total Listings Count


Para los datos de entrenamiento: eliminación de los registros con valor nulo o nan en Price, por no ayudar.
Price                              8

Tanto la media como la desviación típica como los valores de boxplot están más cerca de 1 que de 0 o de 2
Bathrooms                         40
Bedrooms                          18

Tanto la media como la desviación típica como los valores de boxplot están más cerca de 2 que de 1 o de 3
Beds                              37


Por falta de valores para poder hacer algo mejor, eliminamos la columna para evitar mayor complejidad para el modelo.
Square Feet                    10154

## Selección de columnas

Tras haber procesado los datos, hay que hacer la selección de variables que se usarán en el Modelo para predecir el precio.

* Se unsa un RandomForestRegressor con un GridSearchCV para hacer una batería de pruebas y así intentar ver las mejores propiedades a elegir. Una vez tenemos los resultados mostramos el gráfico con las propiedades con más influencia.
* Luego se aplica de nuevo una batería de pruebas con KFold para ver el error que habría con cada una de las propiedades.
* Muestro la gráfica de error y así ver con qué número de variables es bueno quedarse para hacer un modelo equilibrado.

Tras los datos arrojados de error y tras ver la importancia de variables, se escoge de inicio estas 18 variables para el entrenamiento.
- Bedrooms
- Accommodates
- Room Type
- Bathrooms
- Beds
- Guests Included
- Zipcode
- Latitude
- Cleaning Fee
- Extra People
- Calculated host listings count
- Availability 60
- Minimum Nights
- Longitude
- Availability 30
- Security Deposit
- Availability 365
- Availability 90'

Entrenamos el RandomForestRegressor que usamos para la selección de las variables a ver qué resultados nos da el Score:
```
Train:  0.7747069516033211
Test:  0.6333661310539305
```

Tras la primera ejecución con las variables seleccionadas, se decide eliminar las que parecen no tener relación con el precio:
- Si el barrio no ha afectado, la localización no debería influir.
    - Zipcode
    - Latitude
    - Longitude
- Calculated host listings count: recuentos calculados de listados del propietario no debe influir
- La disponibilidad no debe influir
    - Availability 60
    - Availability 30
    - Availability 90
    - Availability 365

Tras eliminar las propiedades elegidas, la puntuación de Test mejora:
```
Train:  0.774984357089286
Test:  0.6436467670507735
```

Aplicamos otros modelos para comprar resultados (Ridge, LinearRegression, Lasso, ElasticNet):

Según los datos de TRAIN y TEST el mejor modelo sería el de RandomForestRegressor.

### RandomForestRegressor
```
Train:  0.774984357089286
Test:  0.6436467670507735
MSE Modelo (train): 710
MSE Modelo (test) : 1.09e+03
RMSE Modelo (train): 26.6
RMSE Modelo (test) : 33.1
```

### LinearRegression
```
Train Score  0.4766626533933088
Test Score  0.495386877504237
MSE Modelo (train): 1650.6657163615525
MSE Modelo (test): 1547.0263489083122
RMSE Modelo (train): 40.62838559876029
RMSE Modelo (test): 39.33225583294597
```

### Ridge
```
Train Score  0.47666138771286326
Test Score  0.4954352796766537
MSE Modelo (train): 1650.6697084621221
MSE Modelo (test): 1546.8779591167372 best alpha: 0.1
RMSE Modelo (train): 40.628434728181716
RMSE Modelo (test): 39.330369425124104 best alpha: 0.1
```

### Lasso
```
Train Score  0.47657858014663446
Test Score  0.49566229056317684
MSE Modelo (train): 1650.9308929763088
MSE Modelo (test): 1546.1819965916181 best alpha: 0.01
RMSE Modelo (train): 40.631648907917935
RMSE Modelo (test): 39.321520781775696 best alpha: 0.01
```

### ElasticNet
```
Train Score  0.4754488729907409
Test Score  0.4952293919536449
MSE Modelo (train): 1654.4941182722923
MSE Modelo (test): 1547.5091629404426 best alpha: 0.01 best l1: 0.9
RMSE Modelo (train): 40.67547317822243
RMSE Modelo (test): 39.338392988789494 best alpha: 0.01 best l1: 0.9
```