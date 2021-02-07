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

# 單筆新增
@app.route('/addMember')
def addMember():
    member_add = Member('Petter', 'PetterPassword')
    db.session.add(member_add)
    db.session.commit()
    return 'OK add'

# 多筆新增
@app.route('/addMembers')
def addMembers():
    # Add List data
    m1 =  Member('Merry', 'MerryPassword')
    m2 =  Member('Jerry', 'JPassword')
    m3 =  Member('Luca', 'LuPassword')
    m4 =  Member('Louis', 'LoPassword')
    m5 =  Member('Tom', 'TomPassword')
    ms = [m1, m2, m3, m4, m5]
    db.session.add_all(ms)
    db.session.commit()
    return 'OK Add Many'

# 查詢
@app.route('/queryMember')
def queryMember():
    # Read Data
    query = Member.query.filter_by(Username='Tom').first()
    memberName = query.Username
    memberPassword = query.Password
    memberCreateTime = str(query.CreateTime)
    return 'Member : ' + memberName + '<br>' + 'Password : ' + memberPassword + '<br>' + memberCreateTime

# 動態查詢
@app.route('/queryMemberByFilter')
def queryMemberByFilter():
    filters = {'Username' : 'Max', 'Password' : 'MaxPassword'}
    query = Member.query.filter_by(**filters).first()
    memberName = query.Username
    memberPassword = query.Password
    memberCreateTime = str(query.CreateTime)
    return 'Member : ' + memberName + '<br>' + 'Password : ' + memberPassword + '<br>' + memberCreateTime

# 排序
@app.route('/queryMemberOrderByCreateTime')
def queryMemberOrderByCreateTime():
    query = Member.query.order_by(Member.id.desc()).all()
    print('desc : ')
    for q in query:
        print(q.Username)

    query = Member.query.order_by(Member.id.asc()).all()
    print('asc : ')
    for q in query:
        print(q.Username)
    return 'see log'

# Delete Data
@app.route('/deleteMember')
def deleteMember():
    query = Member.query.filter_by(Username='Petter').first()
    # print(query.Username)
    if (query != None):
        db.session.delete(query)
        db.session.commit()
    queryAfterDel = Member.query.filter_by(Username='Petter').first()
    if (queryAfterDel == None):
        print(queryAfterDel)
    else:
        print(queryAfterDel.Username)
    
    return 'delete'

# Updata data
@app.route('/updateMember')
def update():
    query = Member.query.filter_by(Username='Max').first()

    # 修改密碼
    query.Password = 'UpdateMaxPassword'
    db.session.commit()
    return 'update'

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