from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Olá Mundo'


@app.route('/nome/<name>')
def hello_name(name):
    return f'Olá {name}'
