from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from exts import db
from models import User

app = Flask(__name__)
DB_URI = 'mysql+pymysql://root:skywalker@127.0.0.1:3306/first_alchemy?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app) 将db生成放到另外模块中
db = db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
