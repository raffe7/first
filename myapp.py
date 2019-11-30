from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
#from models import User

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///root:mysql@127.0.0.1/flask_sql_demo'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config')
db = SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)


@app.route('/')
@app.route('/index/<name>')
def index(name='taozi'):
    user = {'nickname': name}
    return render_template('index.html', title='home', user=user)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

''' @app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error) '''

if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(host='0.0.0.0', port=12345, debug=True)