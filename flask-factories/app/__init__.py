# Flask 初始化設定
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config.config import config

db = SQLAlchemy()

def create_app(config_name):
    
    # 建立應用，Flask 成俗用法，告知Flask你的root在何處。
    app = Flask(__name__)

    # 取得設定檔內容。
    # config_name: 部署實環境變數
    app.config.from_object(config[config_name])

    # db 初始化設定，由app中取得config內容帶入資料庫參數。
    db.init_app(app)

    # route
    @app.route('/')
    def index():
        return 'welcome！ Mode: ' + app.config['MODE']

    return app