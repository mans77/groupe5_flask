from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = "groupe5"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),  unique =True)
    password = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(255))
    website = db.Column(db.String(255))
    street  = db.Column(db.String(255))
    suite = db.Column(db.String(255))
    city = db.Column(db.String(255))
    zipcode = db.Column(db.String(255))
    lng = db.Column(db.String(255))
    lat = db.Column(db.String(255))
    name_company = db.Column(db.String(255))
    catchPrase = db.Column(db.String(255))
    bs = db.Column(db.String(255))
    
class Albums(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    
class Photos(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    url = db.Column(db.String(255))
    thumbnailUrl = db.Column(db.String(255))
    albumId = db.Column(db.Integer(), db.ForeignKey('albums.id'))
    
class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    body = db.Column(db.String(255))
    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    body = db.Column(db.String(255))
    postId = db.Column(db.Integer(), db.ForeignKey('posts.id'))
    
class Todos(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255))
    completed = db.Column(db.String())
    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
if __name__=="__main__":
    db.drop_all()
    db.create_all()
    