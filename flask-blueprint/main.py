from flask import Flask, Blueprint
from view.api import app2

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

app.register_blueprint(app2)
# 加入/pages 的 prefix
# app.register_blueprint(app2, url_prefix='/pages')
