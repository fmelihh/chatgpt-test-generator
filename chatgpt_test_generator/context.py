import inspect
import pydoc
from typing import Dict, Any, Optional
from .expression_search import catch_functions
from .env_operations import load_env, load_declarations

_ENVS: Optional[Dict[str, Any]] = None


def generate_tests_on_background():
    global _ENVS
    if _ENVS is None:
        _ENVS = load_env()

    functions = list()
    python_files = load_declarations()
    for file_path in python_files:
        with open(file_path, "r") as file:
            converted_file = file.read()

        function_names = catch_functions(file_text=converted_file)
        for function_name in function_names:
            func = getattr(pydoc.importfile(file_path), function_name)
            function_snipped = inspect.getsource(func)
            functions.append(function_snipped)
            print(function_snipped)


__all__ = ["generate_tests_on_background"]
