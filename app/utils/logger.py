"""
@title: logger.py
@description: custom logger for monitoring and debugging the errors
    from project.
"""
# standard module import
import logging
from colorlog import ColoredFormatter


def logger():
    log = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    formatter = ColoredFormatter(
        '%(log_color)s %(levelname)-8s [%(filename)s:%(lineno)d - %(funcName)10s()] %(message)s ',
        '%c')
    ch.setFormatter(formatter)
    log.addHandler(ch)
    log.setLevel(logging.DEBUG)
    log.propagate = False
    return log
