# Investigación: Zeppelin

La práctica tiene dos partes:

- Instalación de Zeppelin y configuración de Spark (en la instalación local, no el interprete que viene por defecto) como interprete.
- Realizar un ejercicio que cargue un archivo csv y además nos muestre el número de registros que hay en el archivo.

## Instalación de Zeppelin

Podemos ver el proceso de instalación [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/instalaciones/instalacionzeppelin.md)

## Contar Registros de un fichero csv

Vamos a ubicar el archivo csv en una carpeta del usuario para la posterior carga desde Zeppelin

### Usando SparkSession

En esta opción, vamos a cargar el archivo csv con un esquema y usando un agregado, vamos a mostrar el número de registros existentes en el archivo.

- NoteBook Zeppelin: desde [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/srcejercicios/ejerciciolecturacsv.json) podrá descargar el JSON resultante de la exportación del NoteBook de Zeppelin.

- Imagen del Código fuente: 
![SRC NoteBook Zeppelin Carga CSV](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/EjercicioContarRegistrosCSV.png)

- Imagen del Resultado: 
![Resultado NoteBook Zeppelin Contar Registros CSV](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/EjercicioContarRegistrosCSVResultado.png)

- Vídeo con la ejecución del código (puede que sea mejor descargarlo para visualizarlo)
![NoteBook Zeppelin Running](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/videos/ZeppelinContarRegistrosCSV.mp4)