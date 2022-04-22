from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database'

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "groupe5"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:password@localhost/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

   

    from .views import views
    from .auth import auth
    from .models import Users, Photos, Todos, Albums, Comments, Posts
    

    app.register_blueprint(views, url_prefix ="/")
    app.register_blueprint(auth, url_prefix  ="/")

   
    

    return app 
def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app = app)
        print("Create Database!")

    