import openai
import tokenize
from typing import List, Dict


_TEMPERATURE = 0.5
_MODEL = "text-davinci-003"


def preprocess_functions(functions: Dict[str, List[str]], max_token_count: int) -> Dict[str, List[str]]:
    preprocessed_functions = dict()
    for filename, declared_functions in functions.items():
        for declared_function in declared_functions:
            declared_function = (
                declared_function
                .replace("\n", "")
                .strip()
            )
            token = list(tokenize.generate_tokens(iter([declared_function]).__next__))

            if max_token_count > len(token):
                function_array = preprocessed_functions.get(filename, [])
                function_array.append(declared_function)
                preprocessed_functions[filename] = function_array

    return preprocessed_functions


def generate_prompt(function_input: str) -> str:
    prompt = [
        "Write a pytest test that checks the functionality of a Python function.",
        "Use the following function signature as a starting point:",
        function_input,
    ]
    return '\n'.join(prompt)


def generate_gpt_outputs(api_key: str, max_tokens: int, functions: Dict[str, List[str]]) -> Dict[str, List[str]]:
    responses = dict()
    openai.api_key = api_key
    for filename, declared_functions in functions.items():
        for declared_function in declared_functions:
            try:
                generated_prompt = generate_prompt(function_input=declared_function)
                response = openai.Completion.create(
                    model=_MODEL, prompt=generated_prompt, max_tokens=max_tokens, temperature=_TEMPERATURE
                )["choices"][0]["text"]
                response_array = responses.get(filename, [])
                response_array.append(response)
                responses[filename] = response_array
            except Exception as e:
                print(e)

    return responses
