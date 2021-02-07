from flask import Blueprint

home = Blueprint('home', __name__)

@home.route('/home')
def homeIndex():
    return 'THIS IS HOME INDEX!!'