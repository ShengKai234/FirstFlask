from flask import Blueprint

myapi = Blueprint('myapi', __name__)

@myapi.route('/api_1')
def api_1():
    return 'THIS IS API 1'

@myapi.route('/api_2')
def api_2():
    return 'THIS IS API 2'