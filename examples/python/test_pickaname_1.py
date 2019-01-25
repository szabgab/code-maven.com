import pickaname

def test_pickaname():
    names = pickaname.select_names('../data/names.txt', 3)
    assert len(names) == 3

