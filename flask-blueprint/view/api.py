from flask import Blueprint

app2 = Blueprint('app2', __name__)

@app2.route('/app2')
def showApp2Info():
    return 'Hi App2 is From Blueprint'