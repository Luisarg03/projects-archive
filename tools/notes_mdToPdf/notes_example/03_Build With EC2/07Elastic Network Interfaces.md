## <font color="#EC912D">Elastic Network Interfaces (ENI)</font>

- Una interfaz de red elástica (ENI) es un componente lógico de red que representa una tarjeta de red virtual.
- Permite que la instancia EC2 se comunique en la red con otros hosts, recursos e internet externo.
- Al crear un grupo de seguridad, este se asocia con la interfaz de red elástica.
- El tráfico que intenta conectarse a la interfaz de red elástica debe tener una regla del grupo de seguridad que permita el acceso entrante a la instancia.

### Tipos de Interfaces de Red Elásticas

#### Primaria y Secundaria

- **Primaria:** Se crea por defecto cuando se crea la instancia. No se puede separar ni mover de la instancia en la que fue creada.
- **Secundaria:** Es una interfaz adicional que se crea y se adjunta a la instancia.

**Nota:** El número máximo de interfaces de red elásticas que se pueden usar varía según el tipo de instancia.

### Usos y Configuración de ENI

Un ENI es útil para proporcionar flexibilidad y escalabilidad en la configuración de red de las instancias EC2. Permite que una instancia tenga múltiples interfaces de red, lo que puede ser útil para gestionar tráfico de red diverso o proporcionar aislamiento de red.

**Ejemplo:**

- Tienes una aplicación en una instancia EC2 y necesitas separar el tráfico de administración del tráfico de usuario por razones de seguridad.
- Puedes usar un ENI primario para el tráfico principal de la aplicación y agregar una ENI secundaria para el tráfico administrativo.

#### Configuración de ENI Secundaria

1. Crea una ENI secundaria y la asocias con la misma instancia EC2.
2. Configuras un grupo de seguridad específico para la ENI secundaria que solo permite acceso desde tu red de administración.

**Aquí imagen sobre configuración de ENI**

### Mover una ENI entre Instancias

Mover una ENI entre instancias es útil para mantener la continuidad de la red y la configuración de seguridad cuando necesitas reemplazar o actualizar una instancia EC2 sin interrumpir el servicio.

**Ejemplo:**

- Tienes una aplicación crítica en una instancia EC2 y necesitas realizar mantenimiento en esa instancia o actualizarla. No quieres que el tráfico de red se interrumpa durante este proceso.

**Pasos:**

1. Adjuntar una ENI Secundaria: Crea y adjunta una ENI secundaria a tu instancia actual que tiene configuraciones específicas de red y reglas de seguridad.
2. Mover la ENI a una Nueva Instancia:
    - Antes de realizar el mantenimiento, separa la ENI de la instancia actual.
    - Adjuntas la misma ENI a una nueva instancia que está preparada para tomar el relevo.
3. Redirección Automática de Tráfico:
    - El tráfico de red se redirige automáticamente a la nueva instancia debido a que los atributos y las configuraciones de la ENI se mantienen, lo que garantiza una transición sin interrupciones.

### Dirección IP Pública

Una dirección IP pública permite que las instancias EC2 sean accesibles desde internet. Es esencial para aplicaciones y servicios que necesitan ser accesibles públicamente, como servidores web.

**Asignación de Dirección IP Pública:**

- Las direcciones IP públicas son asignadas desde un pool de direcciones IPv4 públicas de Amazon.
- Estas direcciones no están asociadas con tu cuenta de AWS.
- Cuando una instancia se detiene, hiberna o termina, la dirección IP pública se libera y se asigna una nueva cuando la instancia se reinicia.

**Aquí imagen sobre IP Pública Asignada y Elastic IP**

### Elastic IP (EIP)

Si necesitas una dirección IP pública persistente que puedas asociar y disociar según sea necesario, usa una dirección IP elástica (Elastic IP).

**Usos de Elastic IP:**

- Mantener la misma dirección IP pública para que los usuarios puedan acceder siempre a la misma URL.
- Asociar la Elastic IP a tu instancia EC2 y esta dirección IP permanecerá igual, incluso si paras y reinicias la instancia.

**Costos y Límites:**

- Tienes un límite de cinco Elastic IPs por región por cuenta de AWS.
- Una Elastic IP no está asociada a una instancia, se cobra una pequeña tarifa si no está en uso.

### Traer Tus Propias Direcciones IP (BYOIP) y IPv6

#### BYOIP

Permite traer tus propias direcciones IP a AWS si ya tienes un rango de direcciones IP públicamente enrutable. Esto te permite mantener el control y la consistencia en tu infraestructura de red.

**Ejemplo:**

- Migrar a AWS manteniendo las mismas direcciones IP que tus clientes ya conocen y utilizan para acceder a tus servicios.

#### IPv6

Asociar bloques CIDR IPv6 con tu VPC y subredes es útil para preparar tu infraestructura para el futuro del direccionamiento IP, ya que IPv6 proporciona un espacio de direcciones mucho más grande que IPv4.

**Consideraciones de IPv6:**

- Mantener el control sobre tus direcciones IP y seguir utilizándolas sin cambios para tus usuarios finales.
- IPv6 se asigna automáticamente desde el pool de Amazon.

**Aquí imagen sobre BYOIP y IPv6**

---

### Detalles Clave:

- Las ENI proporcionan flexibilidad y escalabilidad en la red de EC2.
- Es posible mover ENI entre instancias para mantenimiento sin interrumpir el servicio.
- Las direcciones IP públicas permiten la accesibilidad desde internet, mientras que las Elastic IP proporcionan persistencia.
- BYOIP y IPv6 son útiles para mantener el control de la red y prepararse para el futuro.