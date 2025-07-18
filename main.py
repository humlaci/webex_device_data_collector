#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""


from loguru import logger
import sys
from functions import func2
from dotenv import dotenv_values
from my_logger import logger_init


# .env
config = dotenv_values()

# Funtcions and Classes
def main(*args, **kwargs) -> None:
    """Program execution starts here"""
    logger_init()
    
    msg = 'main'
    logger.debug(f'This is a debug message {msg}')
    logger.info(f'This is an info message {msg}')
    logger.warning(f'This is a warning message {msg}')
    logger.error(f'This is an error message {msg}')
    logger.critical(f'This is a critical message {msg}')

    func2()
    
    return None


if __name__ == "__main__":
    main(1,2,3,45,6, s=10, c=20)