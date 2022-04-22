from flask import Blueprint,render_template, request,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database"

auth = Blueprint('auth', __name__)


@auth.route('/posts')
def posts():
    
    return render_template("posts.html")

@auth.route("/albums", methods = ["GET","POST"])
def albums():
    if request.method == "POST":
        title = request.form.get('title')
        post = request.form.get("body")
        print(post)
    return render_template("albums.html")

@auth.route("/todos")
def todos():
   
<<<<<<< HEAD
    return  render_template("todos.html")
=======
    return  render_template("todoss.html")
>>>>>>> 1fc9ef78fd17d98cd880183b0251fce3db728139

@auth.route("/infos")
def infos():
   
    return render_template("infos.html")
