# main.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import make_response
from flask import request
import time

app = Flask(__name__)

# 1. 設定 Cookie
@app.route('/setCookie')
def setCookie():
    resp = make_response('Setting Cookie~~~')
    resp.set_cookie(key='framework', value='flask Cookie Value', expires=time.time()+6*60)
    return resp

# 2. 取得 Cookie
@app.route('/getCookie')
def getCookie():
    framework = request.cookies.get('framework')
    return 'The Framework ' + framework

# 3. 刪除 Cookie
@app.route('/delCookie')
def delCookie():
    resp = make_response('Delete Cookie')
    resp.set_cookie(key='framework', value='', expires=0)
    return resp

@app.route('/login')
def login():
    return 'login'


if __name__ == "__main__":
    app.run()