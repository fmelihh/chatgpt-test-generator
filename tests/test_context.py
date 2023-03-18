from chatgpt_test_generator import generate_tests_on_background


# GPT ->
def deneme(a=0):
    return 1 / a


# GPT ->
def test_deneme():
    import re
    pattern = r"(?<=\n)# GPT ->\s*(def .+):"

