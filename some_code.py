def add_one(x):
    x = x + 1
    return x


def add_two(x):
    x = x + 2
    return x

# Tests


def test_add_one():
    assert add_one(1) == 2


def test_add_two():
    assert add_two(1) == 3
