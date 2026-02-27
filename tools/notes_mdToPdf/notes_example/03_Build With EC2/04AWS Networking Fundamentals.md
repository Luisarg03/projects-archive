## <font color="#EC912D">AWS Networking Fundamentals</font>

#### Regiones y Zonas de Disponibilidad

- Una Región de AWS está compuesta por múltiples Zonas de Disponibilidad, cada una aislada pero conectada por conexiones de alta velocidad y baja latencia.
- **Disponibilidad y Durabilidad**: El diseño de múltiples Zonas de Disponibilidad ofrece fiabilidad y durabilidad de los servicios.
- **Soberanía de Datos**: Los datos almacenados en una Región de AWS no salen de esa Región a menos que se otorgue explícitamente el permiso, cumpliendo con las leyes y normativas locales.
- **Elección y Flexibilidad**: Los usuarios tienen la flexibilidad de elegir en qué Región ejecutar sus aplicaciones.

#### Select REGION

- **Normativas de Datos Locales**: Algunas empresas deben cumplir con regulaciones específicas sobre la localización de datos.
  - Ejemplo: Si tu empresa requiere que todos los datos residan dentro de los límites del Reino Unido, se elige la Región de Londres.
- **Latencia y Entrega de Contenidos**: Seleccionar una Región cercana a la mayoría de tus clientes reduce la latencia y permite una entrega de contenidos más rápida.
- **Disponibilidad de Servicios**: Algunos servicios pueden no estar disponibles en todas las Regiones.
- **Costos Regionales**: Algunas Regiones pueden tener costos diferentes debido a distintos niveles de infraestructura.

#### AZs (Availability Zones)

- Las Zonas de Disponibilidad (Availability Zones) son un componente clave dentro de las Regiones de AWS, diseñadas para ofrecer alta disponibilidad.
- **Elección Flexible**: La ubicación de las Zonas de Disponibilidad está pensada para ofrecer tolerancia a fallos.

![Aquí img]

#### Infraestructura Independiente

- **Componentes**: Cada Zona de Disponibilidad cuenta con alimentación eléctrica, refrigeración y seguridad física independiente.
- **Alta Disponibilidad**: Diseñar aplicaciones para que funcionen en múltiples Zonas de Disponibilidad aumenta la tolerancia a fallos y la disponibilidad.

#### Implementación de EC2

- Al lanzar una instancia de EC2, se usa una máquina virtual en el hardware físico ubicado dentro de una o más zonas de datos que componen una Zona de Disponibilidad.
- **Replicación**: Por defecto, las instancias de EC2 no replican copias a través de las Zonas de Disponibilidad. Sin embargo, puedes crear instancias separadas en cada Zona de Disponibilidad para asegurar que, en caso de que una instancia falle, otra instancia en una Zona de Disponibilidad diferente pueda gestionar las solicitudes de los usuarios.

#### Servicios de AWS y Redundancia

- Algunos servicios de AWS, como Amazon RDS, replican automáticamente copias entre múltiples Zonas de Disponibilidad para tolerancia a fallos y redundancia.
- **Diseño Personalizado**: Aunque EC2 no replica automáticamente, puedes diseñar tu arquitectura para incluir instancias en múltiples AZs, mejorando la disponibilidad y el rendimiento de tu aplicación.

### Resumen Virtual Private Cloud (VPC)

#### Definición de VPC

- Una VPC es una red virtual privada dedicada a tu cuenta de AWS.
- **Configuración Basada en Software**: Se configura y mapea directamente a infraestructura física.
- **Aislamiento Lógico**: Cada VPC está lógicamente aislada de otras redes virtuales en la nube de AWS.

#### Características de la VPC

- Una VPC es como un datacenter en la nube: segmentada en subredes, cada apartamento es una red separada.
- **Gateway**: Permite el acceso dentro y fuera de la VPC.
- **Lanzamiento de Recursos**: Los recursos dentro de la VPC pueden ser lanzados en una AZ, incluso instancias EC2.

#### Tipos de VPC

- **Default VPC**: Se crea automáticamente al abrir una cuenta AWS en cada región.
  - Incluye una subred pública en cada zona de disponibilidad, un Internet Gateway y configuraciones de DNS.
  - Ideal para comenzar rápidamente y lanzar instancias públicas como sitios web simples.
  - Solo puedes tener una Default VPC por región.

- **Nondefault VPC**: Son adicionales y deben ser creadas manualmente.
  - Están aisladas por defecto, sin permitir tráfico de entrada o salida sin configuración explícita.
  - Pueden tener tenancy predeterminado (recursos en hardware compartido) o dedicado (hardware exclusivo para tu cuenta).
  - Puedes tener hasta cinco Nondefault VPCs por región, aunque este límite puede ser aumentado mediante una solicitud a AWS Support.

#### Subnet

- Una subred (o subnet) es una subdivisión lógica de una red IP más grande. Se utiliza para organizar y segmentar una red en partes más pequeñas.
  - **Funcionamiento**: Un subred consiste en una porción más pequeña del rango de direcciones IP de una VPC.
  - **Ubicación**: Cada subred tiene que estar dentro de una única zona de disponibilidad (Availability Zone) y no puede abarcar varias zonas.
  - **Tipos**:
    - **Subred Pública**: Para recursos que necesitan estar conectados a internet, como servidores web.
    - **Subred Privada**: Para recursos que no necesitan acceso directo a internet, como bases de datos.
  - **Dual Stack**: AWS VPC usa IPv4 y también puedes optar por usar IPv6.

### Network ACLs (Access Control Lists)

- Un Network ACL es un filtro de seguridad que controla el tráfico que entra y sale de una subnet.
  - **Funcionamiento**:
    - Se aplica a nivel de la subnet.
    - El ACL por defecto permite todo el tráfico, pero se pueden crear ACLs personalizados que bloquean todo el tráfico hasta que se configuren reglas.
  - **Reglas**:
    - No recuerdan rutas de tráfico, por lo que se necesitan reglas explícitas para tráfico entrante y saliente.
    - Las reglas se procesan en orden desde el número de regla más bajo al más alto, y se detienen al encontrar una coincidencia.

### Security Groups

- Un Security Group es una característica de seguridad asignada a la interfaz de red elástica (ENI) de los recursos de AWS.
  - **Funcionamiento**:
    - Se aplica a nivel de la instancia.
    - Las reglas de los Security Groups se evalúan permitiendo automáticamente el tráfico saliente correspondiente.
    - No tienen reglas explícitas de denegación; si no está explícitamente permitido, está denegado.