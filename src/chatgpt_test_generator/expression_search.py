import re
from typing import List

_FUNCTION_EXPRESSION = r"#\s*GPT\s*->\s*def\s+(\w+)\s*\("


def catch_functions(file_text: str) -> List:
    matches = re.findall(_FUNCTION_EXPRESSION, file_text)
    return matches

