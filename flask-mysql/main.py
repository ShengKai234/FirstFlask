# main.py

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask import make_response
from flask import request
from datetime import datetime

import time


db = SQLAlchemy()

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://db-user:password@localhost:3306/lovemysqldb"

db.init_app(app)

# SQL
@app.route('/sqlConnectTest')
def sqlConnectTest():

    sql_cmd = """
        select *
        from member
        """

    query_data = db.engine.execute(sql_cmd)
    print(query_data)
    for row in query_data:
        print("username:", row['Username'])
    return 'ok test'

@app.route('/indexMember')
def indexMember():
    # Create data
    db.create_all()

    return 'ok'

@app.route('/addMember')
def addMember():
    member_add = Member('Max', 'MaxPassword')
    db.session.add(member_add)
    db.session.commit()
    return 'OK add'

# 模型( model )定義
class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(45), unique=True, nullable=False)
    Password = db.Column(db.String(45), nullable=False)
    CreateTime = db.Column(db.DateTime, default=datetime.now)
    ModifyTime = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password



if __name__ == "__main__":
    app.run()