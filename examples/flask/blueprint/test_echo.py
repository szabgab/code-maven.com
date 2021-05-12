from flask import Flask
from echo import echo_app

def test_app():
    app = Flask(__name__)
    app.register_blueprint(echo_app, url_prefix='/')

    web = app.test_client()

    rv = web.get('/')
    assert rv.status == '200 OK'
    assert '<h2>Echo main</h2>' in rv.data.decode('utf-8')
    assert 'You typed' not in rv.data.decode('utf-8')

    rv = web.get('/run?text=Hello World')
    assert rv.status == '200 OK'
    assert '<h2>Echo main</h2>' in rv.data.decode('utf-8')
    assert 'You typed in Hello World' in rv.data.decode('utf-8')
    
    #print(rv.data)