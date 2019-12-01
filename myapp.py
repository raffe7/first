from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
# import pymysql
# from models import User

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///root:mysql@127.0.0.1/flask_sql_demo'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, nullable=False, unique=True)
    email = db.Column(db.String(120), index=True, nullable=False, unique=True)


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, index=True, unique=True)
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return 'Author: %s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, index=True, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return 'Book: %s' % self.name


@app.route('/')
@app.route('/index/<name>')
def index(name='taozi'):
    user = {'name': name, 'title': 'home'}
    authors = Author.query.all()
    return render_template('index.html', authors=authors, user=user)


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
    # db.drop_all()
    # db.create_all()

    # 生成数据
    ''' au1 = Author(name='杜志建')
    au2 = Author(name='本杰明·富兰克林')
    au3 = Author(name='芭芭拉·明托')
    au4 = Author(name='梁启超')
    au5 = Author(name='丹尼尔·卡尼曼')
    db.session.add_all([au1, au2, au3, au4, au5])
    db.session.commit()
    bk1 = Book(name='高中历史大事年表', author_id=au1.id)
    bk2 = Book(name='富兰克林自传', author_id=au2.id)
    bk3 = Book(name='金字塔原理', author_id=au3.id)
    bk4 = Book(name='李鸿章传', author_id=au4.id)
    bk5 = Book(name='思考，快与慢', author_id=au5.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit() '''

    app.run(host='0.0.0.0', port=12345, debug=True)
