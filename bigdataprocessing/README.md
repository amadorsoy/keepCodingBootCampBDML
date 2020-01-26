# KeepCoding BootCamp Big Data Processing Practical Exercise

# Spark + Kafka + Scala + Zeppelin

## Contextualizar

Voy a seguir la práctica original, además tras escuchar que parte de la idea es que aprendamos a crear nuestro entorno de trabajo, todo se hará en una máquina virtual nueva. El sistema operativo elegido en este caso es Debian 10 64Bits. A partir de una instalación nueva generaré todos los ejercicios que hay que realizar de la práctica.

## Instalación

### Spark

- Instalar Java en Debian (open jdk): por supuesto todo esto con usuario root.
    - sudo apt install default-jdk
    - Descargar Apache Spark, url [aquí](https://apache.brunneis.com/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz)
    - Descomprimir Spark
        ```
        tar xvf spark-2.4.4-bin-hadoop2.7.tgz
        ```
    - Mover el directorio que acabamos de descomprimir a /opt/spark
        ```
        mv spark-2.4.4-bin-hadoop2.7/ /opt/spark
        ```
    - Agregar Spark a las variables de entorno del sistema y activar la nueva configuración. Para ello editamos el archivo ~/.bashrc y agregamos por ejemplo al final las siguientes líneas:
        ```
        export SPARK_HOME=/opt/spark
        export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
        ```
    Después ejecutamos el siguiente comando para activar los cambios en el entorno del usuario:
        ```
        source ~/.bashrc
        ```
    - Aunque toca instalar Scala, antes instalo openjdk la versión 1.8 ya que Scala recomienda tener esa versión instalada. Para ello realizamos:
        ```
        sudo apt install apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common
        wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
        sudo add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
        sudo apt update
        sudo apt install adoptopenjdk-8-hotspot
        ```
    Como ya teníamos una versión de OpenJDK instalada ejecutamos:
    ```update-alternatives --config java```
    Para poder indicar que la opción que queremos de java es la 1.8.
    - Instalar Scala, primero lo hago para entorno de comandos:
    ```
    wget https://downloads.lightbend.com/scala/2.13.1/scala-2.13.1.deb
    dpkg -i scala.2.13.1.deb
    apt update
    apt install scala
    ```

    - Instalar Zeppelin: para eso hacemos los siguientes pasos:
    ```
    wget http://apache.uvigo.es/zeppelin/zeppelin-0.8.2/zeppelin-0.8.2-bin-all.tgz
    tar xvf zeppelin-0.8.2-bin-all.tgz
    mv zeppelin-0.8.2-bin-all/ /opt/zeppelin
    ```
    Una vez hecho esto ya podemos iniciar el servicio, dentro de /opt/zeppelin/:
    ```
    ./bin/zepplin-daemon.sh start
    ```
    Para pararlo el mismo comando pero stop.
    Una vez terminado, podemos ir a http://localhost:8080.
    Importante recordar que si tenemos el puerto ocupado tendríamos que cambiarlo, sino estoy equivocado eso ería en el archivo /opt/zeppelin/conf/zeppelin-site.xml.template
    