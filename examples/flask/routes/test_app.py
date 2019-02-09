import app

def test_static_routes():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/')
    assert rv.status == '200 OK'
    assert b'Main page' == rv.data


    rv = myapp.get('/some/path')
    assert rv.status == '200 OK'
    assert b'A fixed path' == rv.data


def test_one_name():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/user/foobar')
    assert rv.status == '200 OK'
    assert b'The name is foobar' == rv.data

    rv = myapp.get('/user/foo-bar .$')   # accepts any character
    assert rv.status == '200 OK'
    assert b'The name is foo-bar .$' == rv.data

    rv = myapp.get('/user/foo/bar')      # except a slash
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data
    print(rv.data)

    rv = myapp.get('/user/')            # and there must be *something*
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data
    print(rv.data)

def test_one_string():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/title/Hello World!')
    assert rv.status == '200 OK'
    assert b'The title is Hello World!' == rv.data


def test_one_int():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/id/42')
    assert rv.status == '200 OK'
    assert b'The uid is 42' == rv.data

    rv = myapp.get('/id/0')
    assert rv.status == '200 OK'
    assert b'The uid is 0' == rv.data

    rv = myapp.get('/id/x42')            # only accepts digits
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data
    print(rv.data)

    rv = myapp.get('/id/-1')             # not even something that looks a negative int
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

    rv = myapp.get('/id/1.2')            # or a dot
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data


    rv = myapp.get('/id/%D9%A4')         # ٤  ARABIC-INDIC DIGIT FOUR
    assert rv.status == '200 OK'
    assert b'The uid is 4' == rv.data

    rv = myapp.get('/id/٤')              # ٤  ARABIC-INDIC DIGIT FOUR
    assert rv.status == '200 OK'
    assert b'The uid is 4' == rv.data

    rv = myapp.get('/id/߅')              # NKO DIGIT FIVE
    assert rv.status == '200 OK'
    assert b'The uid is 5' == rv.data

def test_float():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/coord-x/4.2')
    assert rv.status == '200 OK'
    assert b'The x coordinate is 4.2' == rv.data

    rv = myapp.get('/coord-x/42')        # does not accept simple digits
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

    rv = myapp.get('/coord-x/1.2.3')     # nor more than one dot
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

    rv = myapp.get('/coord-x/.2')
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

    rv = myapp.get('/coord-x/2.')
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

def test_path():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/place/a/b/c')
    assert rv.status == '200 OK'
    assert b'The location is a/b/c' == rv.data

    rv = myapp.get('/place/a')
    assert rv.status == '200 OK'
    assert b'The location is a' == rv.data

    rv = myapp.get('/place/foo/bar/')
    assert rv.status == '200 OK'
    assert b'The location is foo/bar/' == rv.data

def test_multiple():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/coord/4.2/1.3')
    assert rv.status == '200 OK'
    assert b'The coordinate is (4.2, 1.3)' == rv.data

def test_strange_multiple():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/street/foo/zip/42')
    assert rv.status == '200 OK'
    assert b'The input is foo and 42' == rv.data

def test_ip_address():
    myapp = app.demoapp.test_client()

    rv = myapp.get('/ip/1.2.3.4')
    assert rv.status == '200 OK'
    assert b'The IP is 1.2.3.4' == rv.data

    rv = myapp.get('/ip/1.2.3')
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

    rv = myapp.get('/ip/1.2.0.256')
    assert rv.status == '404 NOT FOUND'
    assert b'404 Not Found' in rv.data

