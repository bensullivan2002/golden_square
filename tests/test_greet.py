from lib.greet import greet


def test_greet():
    greeting = greet("Ben")
    assert greeting == "Hello, Ben!"
