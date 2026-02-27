## <font color="#EC912D">Shared Tenancy</font>

#### Tenencia Compartida (por defecto):

- **Descripción**: Múltiples cuentas de AWS comparten el mismo hardware físico.
- **Uso**: Por defecto, cualquier instancia de EC2 se lanza en un entorno compartido a menos que se especifique lo contrario.
- **Costo**: Es la opción más económica.
- **Seguridad**: Cada instancia está aislada y segura del resto, aunque compartan el mismo hardware físico.
- **Limitaciones**: No soporta instancias que utilicen el modelo Bring Your Own License (BYOL).
- **Soporte**: Soporta instancias Spot y tipos de instancias burstable.

#### Instancia Dedicada

- **Descripción**: Las instancias se ejecutan en hardware dedicado a un solo cliente.
- **Uso**: Permite asegurar que solo tus instancias se ejecuten en el hardware dedicado, aunque las instancias dedicadas pueden compartir hardware con otras instancias de la misma cuenta AWS que no sean dedicadas.
- **Control**: No ofrece visibilidad ni control sobre el hardware subyacente o cómo se colocan las instancias en el hardware.
- **Costo**: Tiene dos componentes de precio, una tarifa por uso por HORA por instancia y una tarifa por REGIÓN dedicada.
- **Seguridad**: Las instancias están dedicadas a un solo cliente, proporcionando un entorno más aislado en comparación con la tenencia compartida.

#### Host Dedicado

- **Descripción**: Un servidor físico donde toda la capacidad de instancia está completamente dedicada al caso del cliente.
- **Uso**: Ideal para cargas de trabajo que requieren cumplimiento, seguridad, o razones de licencias que necesitan servidores dedicados.
- **Control**: Ofrece visibilidad y control sobre cómo se colocan las instancias en el servidor físico y el hardware subyacente. Permite usar el modelo BYOL sin cargos adicionales por el uso de software.
- **Configuración**: Se puede usar el editor de afinidad de instancias del host dedicado, permitiendo un control detallado sobre la infraestructura física.
- **Costo**: Más alto debido al nivel de dedicación y control proporcionado.

### Diferencias Clave

- **Visibilidad y Control**
  - **Instancia Dedicada**: No proporciona visibilidad ni control sobre el hardware subyacente.
  - **Host Dedicado**: Proporciona visibilidad y control sobre el hardware subyacente y la colocación de instancias.

- **Uso de Licencias**
  - **Instancia Dedicada**: No permite usar el modelo BYOL.
  - **Host Dedicado**: Permite usar el modelo BYOL.

- **Costo**
  - **Instancia Dedicada**: Cobro por uso por hora y tarifa por región.
  - **Host Dedicado**: Generalmente más costoso debido al control y dedicación total del hardware.

- **Flexibilidad y Aislamiento**
  - **Instancia Dedicada**: Aislamiento a nivel de hardware para las instancias de un solo cliente, pero sin control sobre la infraestructura.
  - **Host Dedicado**: Aislamiento completo y control sobre la infraestructura física, adecuado para entornos con requisitos estrictos de cumplimiento y licencias.

### Modelo BYOL en AWS

**BYOL (Bring Your Own License)** es un modelo que permite usar utilizar licencias de software previamente adquiridas en las instancias de AWS.

#### Ventajas

- **Ahorro de Costos**: Evita la necesidad de comprar nuevas licencias específicas para la nube.
- **Continuidad**: Utiliza software ya familiar y configurado según las necesidades.
- **Escalabilidad**: Aprovecha la infraestructura escalable de AWS sin cambiar las herramientas y aplicaciones existentes.