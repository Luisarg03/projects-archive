## <font color="#EC912D">Storage Options Amazon EC2</font>

#### Tipos de Almacenamiento de Amazon EC2

**Almacenamiento de Instancias (Instance Store):**
- Almacenamiento temporal que se asigna a tu instancia de EC2.
- Proporciona almacenamiento de bloques a nivel de hardware, adjunto a la instancia.
- **Usos**:
  - Datos que cambian con frecuencia.
  - Almacenamiento de caché.
  - Datos temporales.
- **Características**:
  - Los datos se pierden cuando la instancia se detiene, termina o falla.
  - No se recomienda para datos persistentes.

**Elastic Block Store (EBS):**
- Almacenamiento persistente que se puede adjuntar a instancias EC2.
- Proporciona almacenamiento de bloques a nivel de red.
- **Usos**:
  - Bases de datos.
  - Archivos de logs.
  - Aplicaciones que requieren almacenamiento persistente.
- **Características**:
  - Los volúmenes EBS son replicados dentro de su Zona de Disponibilidad.
  - Se pueden crear snapshots para respaldos y restauraciones.
  - Se pueden cambiar los tipos de volúmenes para ajustar el rendimiento y el costo.
  - Los datos persisten incluso cuando la instancia se detiene.

#### Tipos de Volúmenes EBS

1. **General Purpose SSD (gp3/gp2):**
   - Volúmenes SSD balanceados.
   - **Usos**:
     - Volúmenes de arranque.
     - Volúmenes de datos que necesitan un rendimiento equilibrado.
   - **Rendimiento**:
     - IOPS: Hasta 16,000 (gp3) / 16,000 (gp2).
     - Throughput: Hasta 1,000 MB/s (gp3) / 250 MB/s (gp2).

2. **Provisioned IOPS SSD (io2/io1):**
   - Volúmenes SSD de alto rendimiento.
   - **Usos**:
     - Aplicaciones críticas de negocio.
     - Bases de datos intensivas en I/O.
   - **Rendimiento**:
     - IOPS: Hasta 64,000 (io2) / 64,000 (io1).
     - Throughput: Hasta 1,000 MB/s (io2) / 1,000 MB/s (io1).

3. **Throughput Optimized HDD (st1):**
   - Volúmenes HDD optimizados para throughput.
   - **Usos**:
     - Big data.
     - Data warehouses.
   - **Rendimiento**:
     - Throughput: Hasta 500 MB/s.
     - IOPS: Variado, no tan alto como SSDs.

4. **Cold HDD (sc1):**
   - Volúmenes HDD para datos poco frecuentados.
   - **Usos**:
     - Almacenamiento de archivos.
     - Backups a largo plazo.
   - **Rendimiento**:
     - Throughput: Hasta 250 MB/s.
     - IOPS: Variado, no tan alto como SSDs.

#### EBS Snapshots

- **Backups Incrementales**: Solo los bloques modificados desde el último snapshot.
- **Restauración**: Puedes crear volúmenes EBS a partir de snapshots.
- **Copias Regionales**: Se pueden copiar snapshots entre regiones.

#### Opciones de Almacenamiento de Archivos

**Amazon S3:**
- Almacenamiento de objetos.
- **Usos**:
  - Archivos estáticos.
  - Backups.
  - Data lakes.
- **Características**:
  - Alta durabilidad.
  - Almacenamiento de bajo costo.
  - Acceso vía HTTP/HTTPS.

**Amazon EFS (Elastic File System):**
- Almacenamiento de archivos gestionado.
- **Usos**:
  - Aplicaciones que requieren un sistema de archivos compartido.
  - Archivos de aplicaciones.
- **Características**:
  - Escalable.
  - Acceso concurrente desde múltiples instancias EC2.

**Amazon FSx:**
- Almacenamiento de archivos totalmente gestionado.
- **Usos**:
  - Aplicaciones que requieren sistemas de archivos específicos (Windows, Lustre).
- **Características**:
  - Integración con Active Directory.
  - Rendimiento optimizado para cargas de trabajo específicas.

#### Consideraciones de Seguridad

- **Encriptación**: Tanto en tránsito como en reposo.
- **Control de Acceso**: Utiliza IAM para gestionar permisos.