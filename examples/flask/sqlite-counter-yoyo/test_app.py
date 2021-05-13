from app import create_app
import os

def test_app(tmpdir):
    os.environ['COUNT_DB'] = str(os.path.join(tmpdir, "test.db"))
    print(os.environ['COUNT_DB'])
    web = create_app().test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert '<a href="/something">something</a>' in rv.data.decode('utf-8')

    rv = web.get('/blue')
    assert rv.status == '200 OK'
    #print(rv.data)
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert 'blue : 1' in rv.data.decode('utf-8')
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert '<a href="/blue">blue 1</a>' in rv.data.decode('utf-8')
    assert 'something' not in rv.data.decode('utf-8')


    rv = web.get('/blue')
    assert rv.status == '200 OK'
    #print(rv.data)
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert 'blue : 2' in rv.data.decode('utf-8')
    assert 'red' not in rv.data.decode('utf-8')
    assert 'something' not in rv.data.decode('utf-8')


    rv = web.get('/red')
    assert rv.status == '200 OK'
    #print(rv.data)
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    #assert 'blue : 2' in rv.data.decode('utf-8')
    assert 'red : 1' in rv.data.decode('utf-8')
    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert '<a href="/blue">blue 2</a>' in rv.data.decode('utf-8')
    assert '<a href="/red">red 1</a>' in rv.data.decode('utf-8')
    assert 'something' not in rv.data.decode('utf-8')

# Verify that the two test-cases indeed use different databases
def test_app_clean_db(tmpdir):
    os.environ['COUNT_DB'] = str(os.path.join(tmpdir, "test.db"))
    print(os.environ['COUNT_DB'])
    web = create_app().test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h1>Counter</h1>' in rv.data.decode('utf-8')
    assert '<a href="/something">something</a>' in rv.data.decode('utf-8')
    assert 'blue' not in rv.data.decode('utf-8')
    assert 'red' not in rv.data.decode('utf-8')
