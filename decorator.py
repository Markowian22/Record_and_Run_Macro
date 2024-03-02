from functools import wraps
from time import sleep


def delay(seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(func.__name__)
            sleep(seconds)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def special_key_decorator(func):
    @wraps(func)
    def wrapper(self, key):
        # print(func.__name__)
        if hasattr(key, "name"):
            key = getattr(key, "name")
        else:
            key = key.char
        return func(self, key)

    return wrapper
