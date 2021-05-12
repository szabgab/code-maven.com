import app

def test_app():
    web = app.app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h2>Main</h2>' in rv.data.decode('utf-8')


    rv = web.get('/echo/')
    assert rv.status == '200 OK'
    assert '<h2>Echo main</h2>' in rv.data.decode('utf-8')
    assert 'You typed' not in rv.data.decode('utf-8')

    rv = web.get('/echo/run?text=Hello World')
    assert rv.status == '200 OK'
    assert '<h2>Echo main</h2>' in rv.data.decode('utf-8')
    assert 'You typed in Hello World' in rv.data.decode('utf-8')
    
    #print(rv.data)