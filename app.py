from flask import Flask

app = Flask(__name__)

from rotas import hello, query_string  # noqa
