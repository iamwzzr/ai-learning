from hello import greet


def test_greet() -> None:
    result = greet("GitHub")
    assert result == "Hello, GitHub! Welcome to my AI learning journey."