import os
import toml
from typing import Dict, Any

_CHATGPT_API_KEY_CONSTANT = "CHATGPT_API_KEY"


def load_env() -> Dict[str, Any]:

    root_path = get_root_path()
    settings_conf = toml.load(f"{root_path}/settings.toml")
    if _CHATGPT_API_KEY_CONSTANT not in settings_conf:
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
