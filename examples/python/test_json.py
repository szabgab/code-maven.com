import json
import os

def test_round_trip(tmpdir):
    print(tmpdir)
    filename = tmpdir.join('abc.json')
    print(filename)
    data = {
       'name': 'Foo Bar',
       'grades': [27, 38, 12],
    }

    with open(filename, 'w') as fh:
        json.dump(data, fh)


    with open(filename) as fh:
        new_data = json.load(fh)
    assert data == new_data


