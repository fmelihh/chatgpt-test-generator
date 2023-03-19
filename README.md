## Chatgpt Test Generator

Easy-to-use test generation tool. Powered by ChatGPT.

###  **Project Structure:** 
```
├── main.py
├── poetry.lock
├── pyproject.toml
├── settings.toml
└── tests
```

### **Usage:**

Generates automatic test for all functions with __#GPT ->__ syntax.

_Available syntax rules will increase in next releases._

__main.py__
```
import chatgpt_test_generator


# GPT ->
def search(array: list, number: int):
    for idx, element in enumerate(array):
        if element == number:
            return idx

    return -1


if __name__ == "__main__":
    chatgpt_test_generator.generate_tests_on_background()
    
```

In addition, the settings.toml file should be configured as follows:

__settings.toml__
```
[default]
CHATGPT_API_KEY = "YOUR OPEN-AI API KEY"
```


If main.py is run, it will create tests for functions with GPT -> syntax under /test folder.

```
├── main.py
├── poetry.lock
├── pyproject.toml
├── settings.toml
└── tests
    └── test_main.py
```

__test_main.py__
```
from main import search


def test_search():
    array = [1, 2, 3, 4, 5]
    assert search(array, 3) == 2
    assert search(array, 6) == -1
```

It doesn't matter how complex the project folder is.
```
├── comlex_folder1
│ ├── complex_folder2
│ └── complex_folder4
│   └── example.py
│ └── complex_folder_3
├── main.py
├── poetry.lock
├── pyproject.toml
├── settings.toml
└── tests
    └── test_main.py
```

__example.py__
```
# GPT ->
def divide_numbers(number1: int, number2: int):
    return number1 / number2
```

If I run main.py again, the output will be like this.
```
├── comlex_folder1
│   ├── complex_folder2
│   │   └── complex_folder4
│   │       └── example.py
│   └── complex_folder_3
├── main.py
├── poetry.lock
├── pyproject.toml
├── settings.toml
└── tests
    ├── test_example.py
    └── test_main.py
```

__test_example.py__
```
from comlex_folder1.complex_folder2.complex_folder4.example import divide_numbers


def test_divide_numbers():
    assert divide_numbers(4, 2) == 2
    assert divide_numbers(9, 3) == 3
    assert divide_numbers(2, 4) == 0.5
    assert divide_numbers(-4, -2) == 2
    assert divide_numbers(-9, 3) == -3
    assert divide_numbers(-2, 4) == -0.5
```