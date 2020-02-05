# Instalación de Java - OpenJDK


## Instalar la versión de Java (realmente OpenJDK) por defecto del sistema:
```
apt install default-jdk default-jre
```

## Para instalar la versión 8, que es la recomendada para nuestros trabajos realizamos los siguientes comandos:
    
### Instalar dependencias
```
apt install apt-transport-https ca-certificates wget dirmngr gnupg software-properties-common
```
    
### Obtener la clave pública del repositorio y añadirla
```
wget -qO - https://adoptopenjdk.jfrog.io/adoptopenjdk/api/gpg/key/public | sudo apt-key add -
```
    
### Agregar el repositorio
```
add-apt-repository --yes https://adoptopenjdk.jfrog.io/adoptopenjdk/deb/
```
    
### Actualizar los repositorios para que el sistema de paquetes reconozca lo agregado
```
apt update
```
    
### Instalar la versión deseada de OpenJDK
```
apt install adoptopenjdk-8-hotspot
```
    
### Ejecutar el "configurador" de la versión de java deseada
```
sudo update-alternatives --config java
```
    
### Comprobar la versión de Java para verificar que todo ha salido bien.
```
java -version
```

### Agregar la variable de entorno JAVA_HOME, desde el directorio del usuario 
```
nano .bashrc
```

### Agregar la siguiente línea al final del fichero (es este directorio por querer trabajar con OpenJDK 8):
```
export JAVA_HOME=/usr/lib/jvm/adoptopenjdk-8-hotspot-amd64/
```

### Leer los cambios
```
source .bashrc
```

### Probar la variable creada, desde el terminal escribimos:
```
echo $JAVA_HOME
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Imagen Resultado [url](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/VerificacionInstalacionJava.png):
![Resultado Java Instalado](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/VerificacionInstalacionJava.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------