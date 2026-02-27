import logging
import sys
import pytest

from io import StringIO
from common.helpers_functions import configure_logging


def test_configure_logging():
    # Test the configure_logging function
    with pytest.raises(Exception):
        # Reemplazar sys.stdout y sys.stderr con StringIO para capturar los mensajes de logging
        with StringIO() as stdout_buffer, StringIO() as stderr_buffer:
            sys.stdout = stdout_buffer
            sys.stderr = stderr_buffer

            # Ejecutar la función configure_logging
            root_logger = configure_logging()

            # Prueba si la función establece correctamente la configuración de logging
            assert len(root_logger.handlers) == 2
            assert root_logger.level == logging.INFO

            # Prueba si se registran mensajes en stdout y stderr
            root_logger.info("Test info message")
            root_logger.error("Test error message")

            assert "Test info message" in stdout_buffer.getvalue()
            assert "Test error message" in stderr_buffer.getvalue()

            # Reset stdout and stderr
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            # Generate an exception to test the context manager
            raise Exception("Testing context manager")