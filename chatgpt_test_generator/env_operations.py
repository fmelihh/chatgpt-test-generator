import os
import toml
from typing import Dict, Any, List

_CHATGPT_API_KEY_CONSTANT = "CHATGPT_API_KEY"
# _EXCLUDE_FILE_PATHS = ("chatgpt_test_generator", "tests")
_EXCLUDE_FILE_PATHS = (
    "chatgpt_test_generator",
)


def load_env() -> Dict[str, Any]:

    root_path = get_root_path()
    settings_conf = toml.load(f"{root_path}/settings.toml")
    if _CHATGPT_API_KEY_CONSTANT not in settings_conf["default"]:
        raise ValueError("CHATGPT_API_KEY must be set in settings.toml file.")

    return {
        "TEST_FILE_PATH": f"{root_path}/tests",
        "CHATGPT_API_KEY": settings_conf["default"]["CHATGPT_API_KEY"]
    }


def get_root_path() -> str:
    root_path = os.path.dirname(os.path.abspath(__file__))
    while os.path.exists(os.path.join(root_path, 'main.py')) is False:
        root_path = os.path.dirname(root_path)

    return root_path


def load_declarations(root_path: str = None) -> List[Any]:
    if root_path is None:
        root_path = get_root_path()

    folders = []
    for item in os.listdir(root_path):
        if item in _EXCLUDE_FILE_PATHS:
            continue

        item_path = os.path.join(root_path, item)

        if os.path.isfile(item_path) and item_path.endswith(".py"):
            folders.append(item_path)

        elif os.path.isdir(item_path):
            children = load_declarations(root_path=item_path)
            folders.extend(children)

    return folders


def save_file_to_declared_path(responses: Dict[str, List[str]], test_file_path: str):
    for filename, declared_functions in responses.items():
        with open(f"{test_file_path}/{filename}.py", "w") as python_file:
            python_file.write('\n\n'.join(declared_functions))

