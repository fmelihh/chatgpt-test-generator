import inspect
from typing import Callable, Dict, Any, Optional, List
from .env_operations import load_env

_HASHMAP: Dict[str, str] = {}
_GENERATED_FUNCTIONS_STACK: List[str] = []
_ENVS: Optional[Dict[str, Any]] = None


def function_registerer(func: Callable):
    def wrapper(*args, **kwargs):
        global _ENVS

        if _ENVS is None:
            _ENVS = load_env()

        if func.__name__ not in _GENERATED_FUNCTIONS_STACK:
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
            _GENERATED_FUNCTIONS_STACK.append(func.__name__)
        return func(*args, **kwargs)
    return wrapper


__all__ = ["function_registerer"]
