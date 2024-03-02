from functools import wraps
from time import sleep


def delay(seconds):
    """
    This is a decorator that introduces a delay before calling the decorated function.

    :param seconds: The number of seconds to delay.
    :type seconds: int
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__name__)
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def special_key_decorator(func):
    """
    This is a decorator that handles special keys for the decorated function.

    :param func: The function to decorate.
    :type func: function
    """

    @wraps(func)
    def wrapper(self, key):
        # print(func.__name__)
        if hasattr(key, "name"):
            key = getattr(key, "name")
        else:
            key = key.char
        return func(self, key)

    return wrapper
