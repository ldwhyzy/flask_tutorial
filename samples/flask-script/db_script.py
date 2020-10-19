from flask_script import Manager

db_manager = Manager()


@db_manager.command
def init():
    print('db init')


@db_manager.command
def revision():
    print('db revision')


@db_manager.command
def upgrade():
    print('db upgrade')


@db_manager.command
def downgrade():
    print('db downgrade')