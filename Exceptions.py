import logging
class FlowerNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidQuantityException(Exception):
    def __init__(self, message):
        super().__init__(message)


def logged(exception, mode):
    def decorator(func):
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.ERROR)
        formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        if mode == 'console':
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.DEBUG)
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)
        elif mode == 'file':
            file_handler = logging.FileHandler('logfile.log')
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        else:
            raise ValueError("Invalid logging mode. Use 'console' or 'file'.")

        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger.exception(f"Exception '{e}' occurred in '{func.__name__}'")

        return wrapped

    return decorator
