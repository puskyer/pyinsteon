"""Sample programs to demonstrate pyinsteon."""
import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, 'pyinsteon'))
_LOGGER = logging.getLogger(__name__)
_LOGGER_PYINSTEON = logging.getLogger('pyinsteon')
_LOGGER_MESSAGES = logging.getLogger('pyinsteon.messages')
PATH = os.getcwd()


def set_log_levels(logger='info', logger_pyinsteon='info', logger_messages='info'):
    """Set the log levels of the three logs."""
    _setup_logger(_LOGGER, logger)
    _setup_logger(_LOGGER_PYINSTEON, logger_pyinsteon)
    _setup_logger(_LOGGER_MESSAGES, logger_messages)


def _setup_logger(logger, level):
    _LOGGER.setLevel(_text_to_log_level(level))
    if not logger.hasHandlers():
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)


def _text_to_log_level(log_level_text):
    if log_level_text.lower() == 'debug':
        return logging.DEBUG
    if log_level_text.lower() == 'info':
        return logging.INFO
    if log_level_text.lower() == 'warn':
        return logging.WARN
    if log_level_text.lower() == 'warning':
        return logging.WARNING
    if log_level_text.lower() == 'error':
        return logging.ERROR
    if log_level_text.lower() == 'critical':
        return logging.CRITICAL
    if log_level_text.lower() == 'fatal':
        return logging.FATAL
    return logging.INFO
