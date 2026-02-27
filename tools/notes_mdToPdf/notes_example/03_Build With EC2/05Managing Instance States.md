## <font color="#EC912D">Managing Instance States</font>

#### Encendido y Ciclo de Encendido

Un servidor físico pasa por varios estados durante su ciclo de vida.

**Estados:**
- **Apagado**: El servidor está apagado.
- **Encendido (Cold Booting)**: El servidor se enciende y pasa al estado de funcionamiento (running).
- **Reinicio (Rebooting)**: Si se reinicia, cambia al estado de reinicio.

#### Modos de Ahorro de Energía

- **Sleep (Suspensión)**: Se detienen todas las acciones y se guarda todo en la memoria, usando solo energía mínima.
- **Hibernate (Hibernación)**: Guarda los archivos y aplicaciones abiertas en el disco duro, permitiendo apagar completamente.

#### Ciclo de Vida de una Instancia EC2

- **Pending**: Al lanzarla, brevemente está en estado pendiente mientras se registra.
- **Running**: Luego pasa al estado de funcionamiento. Permanece activa hasta que se detiene o termina.
- **Stopping/Stopped**: Puedes detener una instancia, la cual puede ser reiniciada posteriormente.
- **Terminated**: Una vez terminada, no puede reiniciarse.

#### Estados Adicionales de las Instancias

**Hibernation (Hibernación):**
- **Proceso**: El sistema operativo guarda el contenido de la memoria RAM en el volumen raíz EBS.
- **Al iniciar:**
  1. El volumen raíz EBS se restaura.
  2. Se recargan los contenidos de la RAM.
  3. Los procesos previamente en ejecución se reanudan.
  4. Los volúmenes de datos adjuntos se vuelven a conectar y la instancia retiene su ID.

**Reboot (Reinicio):**
- AWS puede programar reinicios para mantenimiento de hardware.
- Equivalente a un reinicio del sistema operativo.
- Conserva: Nombre DNS público, direcciones IPv4 e IPv6, y datos en volúmenes de almacenamiento de instancias.
- **Nota**: No inicia un nuevo periodo de facturación, a diferencia de detener y arrancar la instancia.

**Retirement (Retiro):**
- Programado cuando AWS detecta fallos irreparables en el hardware.
- **Volumen Raíz EBS**: La instancia se detiene y puede ser reiniciada, migrándose a nuevo hardware.
- **Volumen Raíz de Almacenamiento de Instancia**: La instancia se termina y no puede ser reutilizada.