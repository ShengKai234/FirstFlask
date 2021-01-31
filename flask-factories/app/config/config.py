# 環境設定
import os
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(basedir, db_name)

class BaseConfig:  # 基本配置
    SECRET_KEY = 'THIS IS CONFIG'
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=14)

class DevelopmentConfig(BaseConfig):
    MODE = 'Development'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@ip:3306/tablename'

class TestingConfig(BaseConfig):
    MODE = 'TESTING'
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri("test.db")

config = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
}