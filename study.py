from datetime import datetime

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
manager = Manager(app)
app.config['SECRET_KEY'] = 'hard'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(Form):
    name = StringField('what is your name?', validators=[DataRequired()])

@app.route('/')
def index():
    return render_template('index.html',current_time = datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500




if __name__ == '__main__':
    app.run(debug=True)
