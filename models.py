from exts import db


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
