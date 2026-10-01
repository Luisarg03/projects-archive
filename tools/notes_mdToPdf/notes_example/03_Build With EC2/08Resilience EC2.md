## <font color="#EC912D">Resiliencia y configuracion en Amazon EC2</font>

La resiliencia asegura que tus aplicaciones y datos puedan recuperarse rápidamente de interrupciones, manteniendo la disponibilidad y minimizando el tiempo de inactividad.

#### Ejemplos:

#### Configuración de Terminación y Comportamiento de Apagado

Supongamos que tienes una aplicación crítica en una instancia EC2 que maneja datos sensibles. Para asegurarte de que los datos no se pierdan al terminar la instancia, configuras el atributo `DeleteOnTermination` del volumen raíz a `FALSE`, preservando los volúmenes incluso si la instancia se termina. Además, configuras el comportamiento de apagado a `STOP` para evitar la terminación accidental.

#### Uso de Auto Scaling y Elastic Load Balancing

Para manejar variaciones en el tráfico y asegurar la disponibilidad continua, configuras un grupo de Auto Scaling que lanza nuevas instancias cuando la carga aumenta y las termina cuando disminuye. Usas un Elastic Load Balancer para distribuir el tráfico entre estas instancias, asegurando que el servicio permanezca disponible y eficiente.

#### Protección contra Terminación y Recuperación Automática

Activar la protección contra terminación para instancias críticas evita terminaciones accidentales mediante la consola o API. Configuras también la recuperación automática simplificada para que cualquier fallo en las comprobaciones de estado del sistema inicie automáticamente la recuperación de la instancia, minimizando el tiempo de inactividad.