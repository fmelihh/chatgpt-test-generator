import inspect
from typing import Callable, Dict

_HASHMAP: Dict[str, str] = {}


def function_registerer(func: Callable):
    def wrapper(*args, **kwargs):
        converted_function = inspect.getsource(func)
        converted_function = (
            converted_function
            .replace("@", "")
            .replace(function_registerer.__name__, "")
            .strip("\n")
            .strip()
        )
        _HASHMAP.update({
            func.__name__: converted_function
        })
        return func(*args, **kwargs)
    return wrapper


__all__ = ["function_registerer"]
