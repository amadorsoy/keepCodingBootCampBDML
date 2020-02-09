# Kafka Console Producer

Accedemos al terminal y nos validamos como usuario root (es decir, su) para ejecutar los comandos.

También iremos al directorio de Kafka en el usuario Kafka
```
cd /home/kafka/kafka/bin
```

## Comprobar Kafka Service

Comprobación de funcionamiento correcto de Kafka Service en el sistema
```
systemctl status kafka
```

## Comprobar Zookeeper Service 

Comprobación de funcionamiento correcto de Zookeeper Service en el sistema
```
systemctl status zookeeper
```

## Comprobar existencia de Topics creados

No debería dar ningún resultado, ya que no se ha realizado ningún Topic anteriormente.
```
./kafka-topics.sh --list --zookeeper localhost:2181
```
![Kafka Topics List](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/CheckKafkaZookeeperTopics.png)

## Crear el Topic que se va a usar para la comunicación

Vamos a crear un Topic que usaremos para realizar la comunicación entre el Producer y el Consumer.

Como consideración, se elige crear el Topic con 2 particiones, para prevenir un poco que los datos sean "muchos".

```
./kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 2 --topic topicpractica
``` 

Luego hacemos de nuevo el listado para que veamos si se ha creado correctamente, aunque nos lo indica al crearlo, para eso volvemos a comprobar la existencia de topics creados, con el comando anteriormente citado.

![Kafka Create Topic](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/ZepellinKafkaProducerConsoleCreateTopicAndCheck.png)

## Para eliminar el topic

Por si necesitaramos eliminarlo, sea por la razón que sea, el comando sería:
```
./kafka-topics.sh --zookeeper localost:2181 --delete --topic topicpractica
```

## Generar el Kafka Console Producer (productor)

Tenemos en cuenta que nuestro "Producer" va a ser por consola. Así que usaremos "kafka-console-producer-sh" para generar el "productor". En mi caso tengo el archivo personal.json en "/home/amador/bdproessingfies". Este es el archivo que enviaré con el productor desde la consola. No se adjunta ninguna imagen al proceso, porque realmente no se ve nada, al finalizar el proceso solo vemos el cursor esperando otra nueva instrucción.

```
cat /home/amador/bdprocessingfiles/personal.json | ./kafka-console-producer.sh --broker-list localhost:9092 --topic topicpractica > /dev/null 
```

## Generar el Kafka Console Consumer (consumidor)

Igual que se ejecuta desde el path de instalación de kafka /home/kafka/kafka/bin/ el productor, el consumidor lo ejecutaremos desde el mismo path y siendo también usuario root. Ejecutamos el siguiente comando y deberíamos tener la misma salida por consola que la que vemos en la imagen

```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic topicpractica --from-beginning
```

![Kafka Console Consumer Running](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/KafkaConsoleConsumerViewJsonData.png)


## Crear un Kafka Consumer en Scala

El ejercicio consta de crear en Scala un archivo .scala que lea el contenido de un archivo JSON enviado a través de un Kafka Console Producer y hacer que las palabras que elijamos no aparezcan cuando escribamos el resultado del tratamiento.

### Consideraciones generales

- IDE: se escoge para este ejercicio usar el entorno de desarrollo ofrecido por JetBrains Intellig Idea, para el proyecto se ha tenido que configurar entre otras opciones:
    - JDK: 1.8
    - JARS de Spark, indicarle el directorio desde donde leer los "JARS" de Spark.
    - Scala: versión de uso 2.11.12
    - Importar algunas librerias para trabajar con Kafka en el fichero SBT del proyecto:
        ```
            libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.4.0"% "Provided"
            libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10" % "2.4.0"
            libraryDependencies += "org.apache.spark" %% "spark-sql-kafka-0-10" % "2.4.0"
        ```

- Se pretende eliminar de la cuenta de correo electrónico la palabra ".gov", tampoco queremos mostrar el nombre "Jeanette"y no queremos mostrar el genero "Male".

### Código fuente del proyecto

Para poder ver el código fuente del ejercicio podemos ir [aquí](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/srcejercicios/kcpractica.scala).

Se lee el JSON enviado con Kafka Console Producer con un esquema que ayudará en el tratamiento de la información en modo "SQL".

El resultado final podemos verlo en la siguiente imagen:
![Imagen resumen kafka Consumer](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/KafkaConsumerStringsReplace.PNG)

La ejecución del ejercicio, lo podemos visualizar en el siguiente vídeo (haciendo clic en View Raw se debería ejecutar el vídeo y ver el proceso):
![Vídeo del proceso](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/videos/kafkaconsoleproducerscalaconsumer.mp4)