import full

def test_full(capsys):
    cli = full.MyPrompt();
    cli.cmdqueue = ['exit']
    cli.cmdloop()

    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Welcome! Type ? to list commands\nBye\n'


    cli.cmdqueue = ['help add', 'exit']
    cli.cmdloop()

    out, err = capsys.readouterr()
    assert err == ''
    assert out == 'Welcome! Type ? to list commands\nAdd a new entry to the system.\nBye\n'

