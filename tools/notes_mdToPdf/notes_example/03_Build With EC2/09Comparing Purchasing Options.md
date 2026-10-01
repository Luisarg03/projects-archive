## <font color="#EC912D">Comparing Purchasing Options</font>

#### On-Demand Instances

- **Descripción:** Pagas por capacidad de cómputo por hora o por segundo, sin compromisos a largo plazo ni pagos iniciales. Ideal para cargas de trabajo de corta duración, irregulares o impredecibles que no pueden ser interrumpidas.
- **Uso común:** Desarrollo y prueba de aplicaciones.

#### Savings Plans

- **Descripción:** Modelo de precios flexible que ofrece descuentos a cambio de un compromiso de uso (medido en $/hora) por 1 o 3 años.
- **Tipos:**
  - **Compute Savings Plans:** Se aplica a EC2, AWS Lambda y AWS Fargate.
  - **EC2 Instance Savings Plans:** Se aplica a EC2.
  - **Amazon SageMaker Savings Plans:** Se aplica a Amazon SageMaker.
- **Beneficios:** Mayor flexibilidad para cambiar entre tipos de instancias, regiones y servicios.

#### Reserved Instances (RIs)

- **Descripción:** Descuento en la facturación por el uso de On-Demand Instances a cambio de un compromiso de 1 o 3 años.
- **Tipos:**
  - **Standard RIs:** Descuentos significativos, ideales para cargas de trabajo constantes.
  - **Convertible RIs:** Descuentos menores, permiten cambiar familias de instancias, tipos de SO y tenencias.
- **Uso común:** Cargas de trabajo constantes y sistemas de larga duración.

#### Spot Instances

- **Descripción:** Permiten solicitar capacidad de cómputo EC2 no utilizada con hasta un 90% de descuento sobre el precio On-Demand. Ideal para aplicaciones con tiempos de inicio y fin flexibles, que pueden tolerar interrupciones.
- **Uso común:** Procesamiento en segundo plano, pruebas de aplicaciones con costos bajos.

#### Dedicated Hosts

- **Descripción:** Un servidor físico dedicado para tu uso exclusivo. Ayuda a reducir costos al usar tus licencias de software existentes y cumplir con requisitos de cumplimiento y seguridad. Puede ser comprado On-Demand o como una reserva con hasta un 70% de descuento.

#### Dedicated Instances

- **Descripción:** Instancias EC2 en servidores físicos dedicados exclusivamente a tu cuenta de AWS.
- **Diferencia clave:** Dedicated Hosts ofrecen mayor visibilidad y control sobre la colocación de las instancias en un servidor físico.

### Ejemplos

#### On-Demand Instances

- **Ejemplo:** Imagina que estás desarrollando una nueva aplicación y necesitas instancias EC2 para pruebas. Usar On-Demand Instances te permite lanzar y detener instancias según necesites, pagando solo por el tiempo de uso sin compromisos a largo plazo.

#### Savings Plans

- **Ejemplo:** Supón que tienes una aplicación web que necesitas ejecutar continuamente durante los próximos 3 años. Al optar por un Compute Savings Plan, puedes obtener precios más bajos para tus instancias EC2 y servicios relacionados, ahorrando hasta un 66% en comparación con los precios On-Demand.

#### Reserved Instances (RIs)

- **Ejemplo:** Tienes una base de datos crítica que debe estar en funcionamiento constante. Comprar Standard RIs por 3 años te permite obtener un descuento significativo en comparación con el uso de On-Demand Instances, optimizando costos a largo plazo.

#### Spot Instances

- **Ejemplo:** Tienes una tarea de procesamiento de datos que no es urgente y puede ser interrumpida. Solicitas Spot Instances, aprovechando los precios bajos para ejecutar tu tarea cuando haya capacidad disponible, reduciendo significativamente los costos.

#### Dedicated Hosts

- **Ejemplo:** Trabajas en un sector con estrictos requisitos de cumplimiento y necesitas usar tus propias licencias de software. Al elegir Dedicated Hosts, puedes garantizar que tus instancias EC2 cumplan con las normativas y aprovechar tus licencias existentes, reduciendo costos.

#### Dedicated Instances

- **Ejemplo:** Necesitas asegurar que tus instancias EC2 no compartan hardware con otras cuentas de AWS por motivos de seguridad. Al usar Dedicated Instances, todas tus instancias se ejecutan en servidores físicos dedicados exclusivamente a tu cuenta.

---

### Características y Uso de Spot Instances

- **Descripción:** Spot Instances son ideales para aplicaciones sin estado (stateless), tolerantes a fallos y flexibles.
- **Ejemplos de uso:** Cargas de trabajo en contenedores, integración y entrega continua (CI/CD), servidores web sin estado, computación de alto rendimiento (HPC) y tareas de renderizado.
- **Notas:** Aunque son iguales a las instancias On-Demand en cuanto a funcionalidad, las Spot Instances no garantizan que permanecerán en ejecución el tiempo suficiente para completar tus tareas.
- **Disponibilidad:** La disponibilidad de las Spot Instances puede cambiar según la oferta y la demanda. Esto significa que no siempre puedes obtener la capacidad que solicites de inmediato.
- **Interrupciones:** Debes estar preparado para que las Spot Instances puedan ser interrumpidas en cualquier momento si AWS necesita la capacidad para otras tareas.