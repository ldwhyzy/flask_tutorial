from flask_script import Manager
from app import app, User, db
from db_script import db_manager

manager = Manager(app)
manager.add_command('db', db_manager)


@manager.command
def greet():
    print('hello!')


@manager.option('-n', '--name', dest='name')
@manager.option('-ag', '--age', dest='age')
def add_user(name, age):
    print('add user: (%s, %s)' % (name, age))
    user = User(name=name)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()

# shell
# python manage add_user -n 'name'
