# Instalación y configuración del servicio de Kafka

Partimos de la base de que ya hemos instalado OpenJDK 8, como hemos realizado anteriormente.

## Instalar zookeeperd:
```
apt install zookeeperd
```

## Configurar el servicio zoodeeper al arranque del sistema:
```
systemctl enable zoodeeper
```

## Comprobar el estado del servicio, ver si está activo y sino pues iniciarlo:

- Comprobar el estado del servicio
    ```
    systemctl status zoodeeper
    ```

- En caso que no este iniciado ya:
    ```
    systemctl start zoodeeper
    ```

## Agregar el usuario kafka:
```
sudo useradd kafka -m
```

## Establecer contraseña:

Lo que haremos será introducir la contraseña que queramos, en mi caso kafka.
```
sudo passwd kafka
```

## Agregar el usuario a los usuarios sudo:
```
sudo adduser kafka sudo
```

## Cambiamos al usuario kafka recien agregado al grupo de sudoers:
```
su -l kafka
```

Ahora vamos a usar el home del nuevo usuario para los siguientes pasos

## Descargar la instalación de kafka
Como tengo la versión de scala 2.13.1 descargo kafka_2.13-2.4.0. Recordemos que estamos con el usuario kafka.

### Url de descarga de kafka: [aquí](http://apache.uvigo.es/kafka/2.4.0/kafka_2.13-2.4.0.tgz)
``` 
wget http://apache.uvigo.es/kafka/2.4.0/kafka_2.13-2.4.0.tgz
```
Recordemos que se está descargando en el /home/kafka porque hicimos el cambio de usuario.

## Crear un directorio kafka para hacer la descomprensión y así usarlo como lugar de instalación
```
mkdir kafka
```

## Ir al directorio
```
cd kafka
```

## Descomprimir los archivos para que se situen en /home/kafka/kafka
```
tar -xvzf ~/kafka_2.13-2.4.0.tgz --strip 1
```

## Editar el archivo de configuración que hemos "instalado"

Como estamos situados en /home/kafka/kafka, editamos el archivo de configuración con el siguiente comando
```
nano config/server.properties
```

Y agregamos la siguiente línea al final del archivo, luego guardamos y cerramos el archivo.
```
delete.topic.enable = true
```

## Sistema de inicio de zookeeper

### Configuramos el servicio para kafka de zookeeper

Crear el archivo siguiente con el editor nano
```
nano /etc/systemd/system/zookeeper.service
```

Insertamos el siguiente código:
```
[Unit]
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/con$
ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

### Configurar el servicio de Kafka

Creamos el archivo con el editor nano:
```
nano /etc/systemd/system/kafka.service
```

Insertamos el siguiente código: 
```
[Unit]
Requires=zookeeper.service        
After=zookeeper.service

[Service]
Type=simple
User=kafka
ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties > /home/kafka/kafka/kafka.log 2>&1'
ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```

### Iniciar el servicio

```
systemctl start kafka.service
```

Podemos comprobar si el servicio ha iniciado correctamente con alguno de los dos siguientes comandos:
```
systemctl status kafka.service
```
o
```
jornalctl -u kafka
```
    
### Configurar inicio de kafka al arranque del sistema

Si todo ha ido bien, podemos configurar para que se inicie kafka en cada inicio de sesión:
```
systemctl enable kafka.service
```