from flask import request

from app import app


@app.route('/name_lastname')
def name_lastname():
    name, lastname = request.args['name'], request.args['lastname']
    return f'{name} {lastname}'
