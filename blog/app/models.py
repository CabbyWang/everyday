from . import db
from . import login_manager
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))

    def __repr__(self):
        return 'table users: id:{}, name:{}'.format(self.id, self.username)

    def check(self, password):
        return password == self.password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True)
    content = db.Column(db.Text)
