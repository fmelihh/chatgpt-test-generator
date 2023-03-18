from chatgpt_test_generator import function_registerer


def test_context():
    @function_registerer
    def some_method(a, b):
        return a + b

    some_method(1, 2)

    from chatgpt_test_generator.context import _HASHMAP

    print(_HASHMAP["some_method"])
    assert type(_HASHMAP["some_method"]) is str
