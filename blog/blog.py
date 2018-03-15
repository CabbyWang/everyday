from flask import Flask
from flask import flash
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import data_required
from flask_sqlalchemy import SQLAlchemy

import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a string'   # 防止CRSF攻击

# 数据库是长期存储在计算机内，大量有组织可共享的数据的集合。
# sqlite url(统一资源标识符)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
# 数据库变动时自动更新数据库(默认需要手动提交,告诉数据库要改变数据)
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bootstrap = Bootstrap(app)
manage = Manager(app)


@app.route('/', methods=['Get', 'Post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        use = User.query.filter_by(name=form.name.data)
        if not use:
            one_user = User(name=form.name.data)
            db.session.add(one_user)
        # old_name = session.get('name')
        # if old_name and old_name != form.name.data:
        #     flash('You have change your name.')
        # session['name'] = form.name.data
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name'), form=form, known=session.get('known', False))


@app.route('/hello')
def hello():
    return 'Hello!'


@app.route('/<username>')
def user(username):
    return render_template('user.html', name=username)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(505)
def internal_server_error(e):
    return render_template('505.html'), 505


class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[data_required()])
    submit = SubmitField('submit')


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # optional parameters: primary_key=True, unique=True, default, nullable=True, index=True


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
