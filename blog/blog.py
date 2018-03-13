from flask import Flask, flash
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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a string'   # 防止CRSF攻击
bootstrap = Bootstrap(app)
manage = Manager(app)


@app.route('/', methods=['Get', 'Post'])
def index():
    form = NameForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        old_name = session['name']
        if old_name and old_name != form.name.data:
            flash('You have change your name.')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', name=session.get('name', None), form=form)


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


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()
