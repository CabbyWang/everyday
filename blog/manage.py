from flask_script import Manager
# from flask_sqlalchemy import SQLAlchemy

from app import create_app, db, models

# create app
app = create_app()

manager = Manager(app)
# # create sqlalchemy
# db = SQLAlchemy(app)


@manager.command
def create_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
