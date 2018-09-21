from flask import Blueprint, request

bp = Blueprint('names', __name__)


@bp.route('/name_lastname', methods=['GET', 'POST'])
def name_lastname():
    dct = request.args
    if request.method == 'POST':
        dct = request.form
    name, lastname = dct['name'], dct['lastname']
    return f'{name} {lastname}'


@bp.route('/')
def hello():
    return 'Olá Mundo'


@bp.route('/nome/<name>')
def hello_name(name):
    return f'Olá {name}'
