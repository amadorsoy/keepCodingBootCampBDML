# Instalación de Spark

## Descargar Apache Spark, url [aquí](https://apache.brunneis.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz)
```
wget https://apache.brunneis.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
```

## Descomprimir Spark
```
tar xvf spark-2.4.4-bin-hadoop2.7.tgz
```

## Mover el directorio que acabamos de descomprimir a /opt/spark
```
mv spark-2.4.4-bin-hadoop2.7/ /opt/spark
```

## Agregar Spark a las variables de entorno del sistema y activar la nueva configuración. Para ello editamos el archivo ~/.bashrc y agregamos por ejemplo al final las siguientes líneas:
    
### Editar el archivo de usuario:
```
nano .bashrc
```

### Agregamos lo siguiente al final y salimos del editor guardando los cambios:
```
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```

### Después ejecutamos el siguiente comando para activar los cambios en el entorno del usuario:
```
source .bashrc
```

## Para Iniciar el maestro de Spark, desde el terminal, no haría falta indicar el path ya que lo acabamos de incluir:
```
start-master.sh
```

## Para iniciar el esclavo (en mi caso la maquina virtual es bdprocessing.bootcampbd.keepcoding.com):
```
start-slave.sh spark://bdprocessing.bootcampbd.keepcoding.com:7077
```

Resultado Spark Instalado [url](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/SparkEnDebianPractica.PNG):
![Spark Servicio Activo Maestro - Esclavo](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/SparkEnDebianPractica.PNG)
