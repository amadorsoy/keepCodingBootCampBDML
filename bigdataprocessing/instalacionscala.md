# Instalación Scala

## Primero instalar dependencias:
```
apt install curl
```

## Descargar e instalar Scala
```
wget https://downloads.lightbend.com/scala/2.13.1/scala-2.13.1.deb
dpkg -i scala.2.13.1.deb
apt update
apt install scala
```

## Instalar Scala SBT según la propia documentación de scala-org:
    
``` 
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
curl -sL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x2EE0EA64E40A89B84B2DF73499E82A75642AC823" | sudo apt-key add
sudo apt-get update
sudo apt-get install sbt
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Resultado Scala en Debian [url](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/ScalaDebianPractica.PNG)
![Scala En Debian](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/ScalaDebianPractica.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------