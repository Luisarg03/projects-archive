import sys
import logging
import time

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from awsglue.utils import getResolvedOptions


start_time = time.time()

# ##############
# ## ARGS JOB ##
# ##############
args = getResolvedOptions(sys.argv,
                          ['JOB_NAME'
                           ])

# ##########################
# ## LOGS APP: LEVEL INFO ##
# ##########################
# Configuración del logger raíz
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Configuración del manejador para enviar los mensajes a la salida estándar (stdout)
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)
stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
root_logger.addHandler(stdout_handler)

# Log para inicio de la ejecución
root_logger.info("Iniciando ejecución")


####################################
# ## INIT SESSIONS AND SPARK CONF ##
####################################
sparkappname = "TEST_APP"

# "local[N]": Esto ejecutará Spark en modo local con N hilos.
# "local[*]": Esto ejecutará Spark en modo local utilizando tantos hilos como núcleos tenga la máquina.
# "yarn": Esto ejecutará Spark en un clúster de YARN (Yet Another Resource Negotiator). 

spark_cluster_mode = "yarn"

# nro_instances = 1 # Número de instancias
# vcores_per_instance = 12  # Número de vcores por instancia
# memory_per_instance = 16  # Memoria (GiB) por instancia

nro_instances = 1  # Número de instancias
vcores_per_instance = 4  # Número de vcores por instancia
memory_per_instance = 16  # Memoria (GiB) por instancia
# ebs_storage_per_instance = 64  # Almacenamiento de EBS (GiB) por instancia

# ### parámetros importantes en rendimiento
total_memory = nro_instances * memory_per_instance
total_vcores = nro_instances * vcores_per_instance
executor_memory = int(memory_per_instance * 0.75)  # El 75% de la memoria total se asigna a los executors
executor_cores = vcores_per_instance
executors_per_instance = int(total_memory / executor_memory)
total_executors = nro_instances * executors_per_instance
partitions_per_executor = int(total_vcores * 2)
total_partitions = total_executors * partitions_per_executor
partitions = total_vcores * 2


serializer_buffer_max = '128mb'
memory_fraction = "0.6"
memory_storage_fraction = "0.4"
heartbeat_interval = "8s"
speculation = "true"
speculation_quantile = "0.7"

# Configuración de Spark
conf = SparkConf() \
    .setAppName(sparkappname) \
    .setMaster(spark_cluster_mode) \
    .set("spark.executor.memory", f"{executor_memory}g") \
    .set("spark.executor.cores", f"{executor_cores}") \
    .set("spark.executor.instances", f"{executors_per_instance}") \
    .set("spark.driver.memory", f"{memory_per_instance}g") \
    .set("spark.executor.memoryOverhead", f"{int(executor_memory * 0.25)}g") \
    .set("spark.kryoserializer.buffer.max", f"{serializer_buffer_max}") \
    .set("spark.driver.maxResultSize", f"{memory_per_instance}g") \
    .set("spark.sql.shuffle.partitions", f"{total_partitions}") \
    .set("spark.default.parallelism", f"{total_partitions}") \
    .set("spark.memory.fraction", f"{memory_fraction}") \
    .set("spark.memory.storageFraction", f"{memory_storage_fraction}") \
    .set("spark.executor.heartbeatInterval", f"{heartbeat_interval}") \
    .set("spark.speculation", f"{speculation}") \
    .set("spark.speculation.quantile", f"{speculation_quantile}") \
    .set("spark.core.connection.ack.wait.timeout", "600ms") \
    .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
    .set("spark.sql.hive.convertMetastoreParquet", "true") \
    .set("spark.sql.parquet.fs.optimized.committer.optimization-enabled", "true") \
    .set("spark.sql.sources.partitionOverwriteMode", "dynamic")


spark = SparkSession.builder.config(conf=conf).getOrCreate()
spark.sparkContext.setLogLevel("INFO")

root_logger.info("Session de Spark creada...")
root_logger.info("Spark CONFS:")
for (key, value) in conf.getAll():
    root_logger.info(f"{key} = {value}")
    

spark.stop()