import logging
import sys

from awsglue.utils import getResolvedOptions


# ##############
# ## ARGS JOB ##
# ##############
args = getResolvedOptions(sys.argv,
                          ['JOB_NAME'
                           ])


def configure_logging():
    """
    Configure the logging settings to send messages to the standard output (stdout) and standard error output (stderr).
    """
    
    # ##########################
    # ## LOGS APP: LEVEL INFO ##
    # ##########################
    # Configuración del logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Configuración del manejador para enviar los mensajes a la salida estándar
    # stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(logging.INFO)

    stdout_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
        ))

    root_logger.addHandler(stdout_handler)

    # Agregar un manejador para los logs de nivel ERROR
    # stderr
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setLevel(logging.ERROR)

    stderr_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
        ))

    root_logger.addHandler(stderr_handler)

    return root_logger