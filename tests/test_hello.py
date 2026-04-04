from hello import hello_world


def test_hello_world_returns_string():
    assert isinstance(hello_world(), str)


def test_hello_world_returns_correct_message():
    assert hello_world() == "Hello, World!"
