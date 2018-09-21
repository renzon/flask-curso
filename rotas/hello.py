from app import app


@app.route('/')
def hello():
    return 'Olá Mundo'


@app.route('/nome/<name>')
def hello_name(name):
    return f'Olá {name}'
