from loguru import logger

def func2():
    msg = "func2"
    logger.debug(f'This is a debug message {msg}')
    logger.info(f'This is an info message {msg}')
    logger.warning(f'This is a warning message {msg}')
    logger.error(f'This is an error message {msg}')
    logger.critical(f'This is a critical message {msg}')

