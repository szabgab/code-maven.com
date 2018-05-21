import app

def test_app(capsys):
    input_values = [2, 3]

    def mock_input(s):
        return input_values.pop(0)
    app.input = mock_input

    app.main()

    out, err = capsys.readouterr()

    assert out == 'The result is 5\n'
    assert err == ''
