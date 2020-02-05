# Instalación de Zeppelin

## Descargar la versión de todo incluido:
```
wget http://apache.uvigo.es/zeppelin/zeppelin-0.8.2/zeppelin-0.8.2-bin-all.tgz
```

## Descomprimir el archivo:
```
tar xvf zeppelin-0.8.2-bin-all.tgz
```

## Mover el contenido del directorio a /opt/zeppelin
```
mv zeppelin-0.8.2-bin-all/ /opt/zeppelin
```

## Copiar fichero de configuración para cambiar el puerto:
```
cp /opt/zeppelin/conf/zeppelin-env.sh.template /opt/zeppelin/conf/zeppelin-env.sh
```

## Agregar la siguiente línea al final del fichero:
```
export ZEPPELIN_PORT=8100
```

## Una vez guardados los cambios ya podemos usar sin problemas el demonio de zeppelin para iniciar el servicio o pararlo

### Iniciar:
```
/opt/zeppelin/bin/zeppelin-daemon.sh start
```
### Parar:
```
/opt/zeppelin/bin/zeppelin-daemon.sh stop
```

### Chequear el servicio
Cuando se inicia solo tenemos que ir a la url: http://localhost:8100. Es así porque hemos cambiado el puerto anteriormente

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Resultado Zeppelin en Navegador [url](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/ZeppelinEnDebianPractica.PNG)
![Zeppelin NoteBook](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/ZeppelinEnDebianPractica.PNG)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Configurar nuestro Spark local, como el interprete de Spark en Zeppelin

Este proceso se hará con una configuración nueva para evitar "romper" el que viene en la instalación por defecto en los interpretes.

### Ir al menú de usuario (en nuestro caso anonymous)

Situado en la parte superior derecha de la plataforma web que se nos abre al acceder a la url del servicio

### Seleccionar la parte de Interprete

Del menú que se despliega, seleccionar Interprete

### Hacer clic en +Create

En los siguientes campos establecer los valores indicados

- Interpreter Name: SparkLocal
- Interpreter Group: Spark

### Guardar y volver al Home para verificar que ha cargado los cambios.

Hay veces que no coge bien los cambios, para asegurarnos hacemos clic en el home y volvemos a entrar al menú de Interprete en anonymous

### Editar la configuración recien creada

Vamos de nuevo a la sección Interprete del menú de usuario. Buscamos SparkLocal y cuando nos aparezca hacemos clic en Edit.

- En el último cuadro de texto antes de Dependencias ponemos SPARK_HOME a la izquierda y /opt/spark en la derecha.
- Guardamos los cambios y hacemos clic en restart del interprete.

Ya podremos usar nuestro Spark en Local en Zeppelin

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Resultado configurado Spark Local en Zeppelin [url](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/SparkLocalEnZeppelin.png)
![Spark Local 2.4.4 en Zeppelin](https://github.com/amadorsoy/keepCodingBootCampBDML/blob/master/bigdataprocessing/images/SparkLocalEnZeppelin.png)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------