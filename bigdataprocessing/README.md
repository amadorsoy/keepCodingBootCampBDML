# KeepCoding BootCamp Big Data Processing Practical Exercise

# Spark + Kafka + Scala + Zeppelin

## Contextualizar

Voy a seguir la práctica original, además tras escuchar que parte de la idea es que aprendamos a crear nuestro entorno de trabajo, todo se hará en una máquina virtual nueva. El sistema operativo elegido en este caso es Debian 10 64Bits. A partir de una instalación nueva generaré todos los ejercicios que hay que realizar de la práctica.

## Instalación

### Java

Una vez instalada la maquina virtual con Debian 10 como sistema operativo realizamos los siguientes comandos como usuario root:
- Instalar la versión de Java (realmente OpenJDK) por defecto del sistema:
    ```
    apt install default-jdk default-jre
    ```
- Para instalar la versión 8, que es la recomendada para nuestros trabajos realizamos los siguientes comandos:
    - Instalar dependencias
        ```
        apt install apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common
        ```
    - Obtener la clave pública del repositorio y añadirla
        ```
        wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
        ```
    - Agregar el repositorio
        ```
        add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
        ```
    - Actualizar los repositorios para que el sistema de paquetes reconozca lo agregado
        ```
        apt update
        ```
    - Instalar la versión deseada de OpenJDK
        ```
        apt install adoptopenjdk-8-hotspot
        ```
    - Ejecutar el "configurador" de la versión de java deseada
        ```
        sudo update-alternatives --config java
        ```
    - Comprobar la versión de Java para verificar que todo ha salido bien.
        ```
        java -version
        ```
    - Agregar la variable de entorno JAVA_HOME, desde el directorio del usuario 
        ```
        nano .bashrc
        ```
    - Agregar la siguiente línea al final del fichero (es este directorio por querer trabajar con OpenJDK 8):
        ```
        export JAVA_HOME=/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64/
        ```
    - Leer los cambios
        ```
        source .bashrc
        ```
    - Probar la variable creada, desde el terminal escribimos:
        ```
        echo $JAVA_HOME
        ```

### Spark

- Descargar Apache Spark, url [aquí](https://apache.brunneis.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz)
    ```
    wget https://apache.brunneis.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz
    ```
- Descomprimir Spark
    ```
    tar xvf spark-2.4.4-bin-hadoop2.7.tgz
    ```
- Mover el directorio que acabamos de descomprimir a /opt/spark
    ```
    mv spark-2.4.4-bin-hadoop2.7/ /opt/spark
    ```
- Agregar Spark a las variables de entorno del sistema y activar la nueva configuración. Para ello editamos el archivo ~/.bashrc y agregamos por ejemplo al final las siguientes líneas:
    
    Editar el archivo de usuario:
        ```
        nano .bashrc
        ```

    Agregamos lo siguiente al final y salimos del editor guardando los cambios:
        
        ```
        export SPARK_HOME=/opt/spark
        export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
        ```

    Después ejecutamos el siguiente comando para activar los cambios en el entorno del usuario:
        ```
        source .bashrc
        ```

- Para Iniciar el maestro de Spark, desde el terminal, no haría falta indicar el path ya que lo acabamos de incluir:
    ```
    start-master.sh
    ```
- Para iniciar el esclavo:
    ```
    start-slave.sh spark://bdprocessing.bootcampbd.keepcoding.com:7077
    ```



### Scala 

- Primero instalar dependencias:
    ```
    apt install curl
    ```
- Descargar e instalar Scala
    ```
    wget https://downloads.lightbend.com/scala/2.13.1/scala-2.13.1.deb
    dpkg -i scala.2.13.1.deb
    apt update
    apt install scala
    ```

- Instalar Scala SBT según la propia documentación de scala-org:
    ``` 
    echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
    curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
    sudo apt-get update
    sudo apt-get install sbt
    ```


### Zeppelin

- Descargar la versión de todo incluido:
    ```
    wget http://apache.uvigo.es/zeppelin/zeppelin-0.8.2/zeppelin-0.8.2-bin-all.tgz
    ```
- Descomprimir el archivo:
    ```
    tar xvf zeppelin-0.8.2-bin-all.tgz
    ```
- Mover el contenido del directorio a /opt/zeppelin
    ```
    mv zeppelin-0.8.2-bin-all/ /opt/zeppelin
    ```
- Copiar fichero de configuración para cambiar el puerto:
    ```
    cp /opt/zeppelin/conf/zeppelin-env.sh.template /opt/zeppelin/conf/zeppelin-env.sh
    ```
- Agregar la siguiente línea al final del fichero:
    ```
    export ZEPPELIN_PORT=8100
    ```
- Una vez guardados los cambios ya podemos usar sin problemas el demonio de zeppelin para iniciar el servicio o pararlo
    - Iniciar:
        ```
        /opt/zeppelin/bin/zeppelin-daemon.sh start
        ```
    - Parar:
        ```
        /opt/zeppelin/bin/zeppelin-daemon.sh stop
        ```
- Cuando se inicia solo tenemos que ir a la url: http://localhost:8100. Es así porque hemos cambiado el puerto anteriormente

- Configurar nuestro Spark local, como el interprete de Spark en Zeppelin (pero con una configuración nueva para no romper el que viene en la instalación por defecto.)

    * Ir al menú de usuario (en nuestro caso anonymous)
    * Seleccionar la parte de Interprete
    * Hacer clic en +Create
        * Interpreter Name: SparkLocal
        * Interpreter Group: Spark
        * Guardar y volver al Home para verificar que ha cargado los cambios.
        * Vamos de nuevo a la sección Interprete del menú de usuario.
        * Buscamos SparkLocal y cuando nos aparezca hacemos clic en Edit.
        * En el último cuadro de texto antes de Dependencias ponemos SPARK_HOME a la izquierda y /opt/spark en la derecha.
        * Guardamos los cambios y hacemos clic en restart del interprete.
        * Ya podremos usar nuestro Spark en Local en Zeppelin

    