from package1.module1 import hello_world

pytest_plugins = ["docker_compose"]


def test_hello_world():
    assert hello_world() == 'Hello, World!'
