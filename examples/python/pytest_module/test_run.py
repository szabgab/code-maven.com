def setup_module(module):
    print(dir(module))

def teardown_module(module):
    print(dir(module))

def test_run():
    print("Runnin the test_run function")
    assert True
    #assert False
