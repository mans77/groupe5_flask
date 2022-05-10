from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from  flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB_NAME = 'flask'

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "groupe5"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:groupe5@localhost/flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    

    from .views import views
    from .auth import auth
    from .models import Users, Photos, Todos, Albums, Comments, Posts
    

    app.register_blueprint(views, url_prefix ="/")
    app.register_blueprint(auth, url_prefix  ="/")
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app 

        
        

    