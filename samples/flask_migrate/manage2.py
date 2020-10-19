## flask_migrate比直接使用alembic便利在不用额外进行配置db.URI db.models
##python manage2.py db init
##python manage2.py db migrate
##python manage2.py db upgrade
##如果app和models(user, article..)在不同模块中，需要在app模块import这些需要映射到数据库的模型，否则db migrate会no changes in schema detected


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime

app = Flask(__name__)
DB_URI = 'mysql+pymysql://root:skywalker@127.0.0.1:3306/first_alchemy?charset=utf8'
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manage = Manager(app)
Migrate(app, db)
manage.add_command('db', MigrateCommand)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<User(name=%s)>' % self.name


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))
    create_time = db.Column(db.DateTime, default=datetime.now)

    publisher = db.relationship('User', backref='articles')

    def __repr__(self):
        return '<Article(title=%s)>' % self.title


if __name__ == '__main__':
    manage.run()
