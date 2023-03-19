import inspect
import pydoc
from typing import Dict, Any, Optional
from .expression_search import catch_functions
from .env_operations import load_env, load_declarations, save_file_to_declared_path
from .interaction import preprocess_functions, generate_gpt_outputs

_ENVS: Optional[Dict[str, Any]] = None


def generate_tests_on_background(max_tokens: int = 1500):
    global _ENVS
    if _ENVS is None:
        _ENVS = load_env()

    functions = dict()
    python_files = load_declarations()

    for file_path in python_files:
        with open(file_path, "r") as file:
            converted_file = file.read()

        filename = f'test_{file_path.split("/")[-1].split(".")[0]}'
        function_names = catch_functions(file_text=converted_file)
        for function_name in function_names:
            func = getattr(pydoc.importfile(file_path), function_name)
            function_snipped = inspect.getsource(func)
            if len(function_snipped) > 0:
                function_array = functions.get(filename, [])
                function_array.append(function_snipped)

                functions[filename] = function_array

    functions = preprocess_functions(functions=functions, max_token_count=max_tokens)
    if len(functions) == 0:
        return

    chatgpt_outputs = generate_gpt_outputs(
        api_key=_ENVS["CHATGPT_API_KEY"],
        max_tokens=max_tokens,
        functions=functions
    )

    if len(chatgpt_outputs) == 0:
        return

    save_file_to_declared_path(responses=chatgpt_outputs, test_file_path=_ENVS["TEST_FILE_PATH"])


__all__ = ["generate_tests_on_background"]
