from flask import Blueprint, request

bp = Blueprint('names', __name__)


@bp.route('/name_lastname')
def name_lastname():
    name, lastname = request.args['name'], request.args['lastname']
    return f'{name} {lastname}'


@bp.route('/')
def hello():
    return 'Olá Mundo'


@bp.route('/nome/<name>')
def hello_name(name):
    return f'Olá {name}'
