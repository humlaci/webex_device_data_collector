#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Module docstring."""

from dotenv import dotenv_values
from loguru import logger
import sys

# Module Constants
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

# Module "Global" Variables
log_level = "DEBUG"

# .env
config = dotenv_values()

# Funtcions and Classes
def logger_init() -> None:
    """logger init"""
    
    # configure log_level
    try:
        if config["LOG_LEVEL"] and config["LOG_LEVEL"] in LOG_LEVELS:
            log_level = config["LOG_LEVEL"]
        else:
            log_level = "DEBUG"
    except KeyError as e:
        log_level = "DEBUG"
    
    # remove default logger
    logger.remove()
    
    # log to console
    logger.add(sys.stdout, level=log_level)
    
    # log everything to app.log
    logger.add("app.log", level=log_level)
    
    # functions.py will be logged functions.log also (and app.log as wells) (func2 comes from functions.py)
    logger.add("functions.log", colorize=True, format="{time} | {level} | {module}:{function}:{line} - {message}", filter="api_calls", level=log_level)
    
    return None

def main(*args, **kwargs) -> None:
    """Nothing happesns here"""
    return None


if __name__ == "__main__":
    main()