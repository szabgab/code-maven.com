import app


def test_app():
    random_numbers = [19, 23]
    app.random.randrange = lambda n : random_numbers.pop(0)

    assert app.main() == 42
